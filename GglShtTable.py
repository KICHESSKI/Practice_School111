from typing import Dict, List, Union
import pygsheets

class GoogleTable:
    """Класс для работы с Google Sheet."""
    def __init__(
        self, credence_service_file:str = "", googlesheet_file_url:str = ""
    ) -> None:
        """Инициализирует класс.
        Args:
            credence_service_file (str): Путь до сервисного файла credence.json (Google Sheet API).
            googlesheet_file_url (str): Ссылка на Google Sheet.
        Returns:
        """
        self.credence_service_file = credence_service_file
        self.googlesheet_file_url = googlesheet_file_url

    def _get_googlesheet_by_url(
        self, googlesheet_client: pygsheets.client.Client
    ) -> pygsheets.Spreadsheet:
        """Получает Google.Docs таблицу по ссылке на документ."""
        sheets: pygsheets.Spreadsheet = googlesheet_client.open_by_url(
            self.googlesheet_file_url
        )
        return sheets.sheet1

    def _get_googlesheet_client(self):
        """Авторизуется с помощью сервисного ключа и
        возвращает клиентский объект Google Docs.
        """
        return pygsheets.authorize(
            service_file=self.credence_service_file
        )

    def search_mon(
            self,
            data: List[List[Union[str, bool]]],
            search_col: int = 1,
            mon_col: int = 2,
    ) -> Union[List[str], int]:
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            find_cell = wks.find(data, matchEntireCell=True, cols=(search_col, search_col))[0]
        except:
            return -1
        find_cell_row = find_cell.row
        rasp = wks.get_value((find_cell_row, mon_col))
        return [rasp]

    def search_tue(
            self,
            data: List[List[Union[str, bool]]],
            search_col: int = 1,
            tue_col: int = 3,
    ) -> Union[List[str], int]:
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            find_cell = wks.find(data, matchEntireCell=True, cols=(search_col, search_col))[0]
        except:
            return -1
        find_cell_row = find_cell.row
        rasp = wks.get_value((find_cell_row, tue_col))
        return [rasp]

    def search_wen(
            self,
            data: List[List[Union[str, bool]]],
            search_col: int = 1,
            wen_col: int = 4,
    ) -> Union[List[str], int]:
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            find_cell = wks.find(data, matchEntireCell=True, cols=(search_col, search_col))[0]
        except:
            return -1
        find_cell_row = find_cell.row
        rasp = wks.get_value((find_cell_row, wen_col))
        return [rasp]

    def search_thur(
            self,
            data: List[List[Union[str, bool]]],
            search_col: int = 1,
            thur_col: int = 5,
    ) -> Union[List[str], int]:
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            find_cell = wks.find(data, matchEntireCell=True, cols=(search_col, search_col))[0]
        except:
            return -1
        find_cell_row = find_cell.row
        rasp = wks.get_value((find_cell_row, thur_col))
        return [rasp]


    def search_fri(
            self,
            data: List[List[Union[str, bool]]],
            search_col: int = 1,
            fri_col: int = 6,
    ) -> Union[List[str], int]:
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            find_cell = wks.find(data, matchEntireCell=True, cols=(search_col, search_col))[0]
        except:
            return -1
        find_cell_row = find_cell.row
        rasp = wks.get_value((find_cell_row, fri_col))
        return [rasp]


    def search_sat(
            self,
            data: List[List[Union[str, bool]]],
            search_col: int = 1,
            sat_col: int = 7,
    ) -> Union[List[str], int]:
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            find_cell = wks.find(data, matchEntireCell=True, cols=(search_col, search_col))[0]
        except:
            return -1
        find_cell_row = find_cell.row
        rasp = wks.get_value((find_cell_row, sat_col))
        return [rasp]