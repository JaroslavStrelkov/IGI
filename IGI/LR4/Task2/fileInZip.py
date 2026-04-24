import zipfile


class FileInZIP:
    @staticmethod
    def zip_machen(file_name, zip_file_name):
        with zipfile.ZipFile(zip_file_name, "w") as zip:
            zip.write(file_name)

    @staticmethod
    def get_zip_info(zip_name):
        with zipfile.ZipFile(zip_name, "r") as zip:
            for file in zip.infolist():
                print(f"Имя файла: {file.filename}, размер файла: {file.file_size}, дата файла: {file.date_time}")