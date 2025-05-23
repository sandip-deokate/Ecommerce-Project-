import os.path

from pageObjects.BomToolPage.bomToolPageElements import BomToolPageElements
class bomToolPageHelpers:
    def __init__(self,driver):
        self.Elements=BomToolPageElements(driver)

    def get_bom_tool_page_title(self):
         bom_page_title=self.Elements.get_bom_tool_page_elements()
         return bom_page_title.text

    def upload_bom_file(self):
        upload_bom = self.Elements.get_upload_bom()
        file_path = os.path.join(os.path.abspath(os.curdir), 'testData', 'BomShort.xlsx')
        upload_bom.send_keys(file_path)



