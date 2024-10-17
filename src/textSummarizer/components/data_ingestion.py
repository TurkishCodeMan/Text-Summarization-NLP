import os
from pathlib import Path
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from tqdm import tqdm



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            with tqdm(
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                miniters=1,
                desc="Downloading",
            ) as progress:

                def progress_hook(block_num, block_size, total_size):
                    progress.total = total_size  # Toplam boyut
                    progress.update(block_size)  # İlerleme güncellemesi

                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file,
                    reporthook=progress_hook,  # İlerleme çubuğu için fonksiyon
                )

            logger.info(
                f"{filename} download completed with following info:\n{headers}"
            )
        else:
            file_size = get_size(Path(self.config.local_data_file))
            logger.info(f"File already exists with size: {file_size}")

    def extract_zip_file(self):
        """
        zip_file_path:str
        Extracts the zip file to the specified directory
        Function return None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)