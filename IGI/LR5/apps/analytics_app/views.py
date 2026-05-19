from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth, TruncYear
from apps.orders.models import Order, OrderItem
from apps.cars.models import Car, CarCategory
import statistics
import matplotlib.pyplot as plt
import numpy as np
import os

@login_required
def analytics_dashboard(request):
    if not request.user.is_superuser:

        return render(request, 'analytics/no_access.html')

    total_revenue = (Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0)

    popular_car = (OrderItem.objects.values('car__name').annotate(total=Sum('quantity')).order_by('-total').first())

    unpopular_car = (OrderItem.objects.values('car__name').annotate(total=Sum('quantity')).order_by('total').first())

    clients_by_city = (Order.objects.values('customer__profile__city').annotate(total=Count('id')).order_by('-total'))

    sales = list(Order.objects.values_list('total_price',flat=True))

    average_sale = 0
    median_sale = 0

    if sales:
        average_sale = round(statistics.mean(sales),2)
        median_sale = statistics.median(sales)

    price_list = (Car.objects.values('category__name').annotate(total_price=Sum('price')))

    monthly_by_category = (OrderItem.objects.annotate(month=TruncMonth('order__sale_date')).values('month','car__category__name').annotate(total=Sum('quantity')).order_by('month'))

    yearly_sales = (Order.objects.filter(sale_date__isnull=False).annotate(year=TruncYear('sale_date')).values('year').annotate(total=Sum('total_price')).order_by('year'))

    monthly_sales = (Order.objects.filter(sale_date__isnull=False).annotate(month=TruncMonth('sale_date')).values('month').annotate(total=Sum('total_price')).order_by('month'))

    months = []
    totals = []

    for item in monthly_sales:
        if item['month'] is not None:
            months.append(item['month'].strftime('%m/%Y'))
            totals.append(float(item['total'] or 0))

    os.makedirs('media/charts', exist_ok=True)

    plt.figure(figsize=(8, 4))

    plt.plot(months,totals,marker='o')

    plt.title('Продажи по месяцам')
    plt.xlabel('Месяц')
    plt.ylabel('Сумма')

    chart_path = ('media/charts/monthly_sales.png')

    plt.savefig(chart_path)
    plt.close()

    category_stats = (OrderItem.objects.values('car__category__name').annotate(total=Sum('quantity')))

    labels = []
    sizes = []

    for item in category_stats:
        labels.append(item['car__category__name'])
        sizes.append(item['total'])

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Продажи по категориям')

    pie_chart_path = ('media/charts/category_pie.png')

    plt.savefig(pie_chart_path)
    plt.close()

    trend_chart = None

    if len(totals) > 1:
        x = np.arange(len(totals))
        y = np.array(totals)
        coefficients = np.polyfit(x, y, 1)
        trend = np.poly1d(coefficients)
        future_x = np.arange(len(totals) + 3)
        future_y = trend(future_x)
        plt.figure(figsize=(8, 4))
        plt.plot(x, y, marker='o')
        plt.plot(future_x, future_y, linestyle='dashed')
        plt.title('Тренд и прогноз продаж')
        trend_path = ('media/charts/trend.png')
        plt.savefig(trend_path)
        plt.close()
        trend_chart = ('/media/charts/trend.png')

    return render(request,'analytics/dashboard.html',
        {
            'total_revenue': total_revenue,
            'popular_car': popular_car,
            'unpopular_car': unpopular_car,
            'clients_by_city': clients_by_city,
            'average_sale': average_sale,
            'median_sale': median_sale,
            'chart_url': '/media/charts/monthly_sales.png',
            'price_list': price_list,
            'monthly_by_category': monthly_by_category,
            'yearly_sales': yearly_sales,
            'pie_chart': '/media/charts/category_pie.png',
            'trend_chart': trend_chart,
        }
    )
