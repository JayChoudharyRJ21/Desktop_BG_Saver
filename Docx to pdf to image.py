from docx2pdf import convert
import os , ctypes,pdf2image
from pdf2image import convert_from_path


def Date_Module():
    from datetime import date
    Months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August", 9:"September",10:"October",11:"November",12:"December"}
    today = date.today()
    Month = Months[today.month]
    Day = today.day
    Year = today.year
    return (f'{Month} {Day} {Year}')
Date = Date_Module()    

def set_wallpaper(image_path):
    # Select the appropriate SPI constant for setting the desktop background
    SPI_SETDESKWALLPAPER = 0x0014
    # Call the SystemParametersInfo function from user32.dll
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    
def init():
    #-------------> Image 2 Wall_Paper <-------------#
    def Date_Module():
        from datetime import date
        Months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August", 9:"September",10:"October",11:"November",12:"December"}
        today = date.today()
        Month = Months[today.month]
        Day = today.day
        Year = today.year
        return (f'{Month} {Day} {Year}')
    Date = Date_Module()
        
    def set_wallpaper(image_path):
        # Select the appropriate SPI constant for setting the desktop background
        SPI_SETDESKWALLPAPER = 0x0014
        # Call the SystemParametersInfo function from user32.dll
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

    #-----------Paths File_Names------------------#
    #doc_path = "C:/Users/Jugal/Desktop/Daily Timetable/Total Tasks.docx"
    doc_path = "C:/Users/Jugal/Desktop/Daily Timetable/TIME TABLE00.docx"
    pdf_output = "C:/Users/Jugal/Desktop/Daily Timetable/TIME TABLE_new.pdf"
    # =============================================================================
    # image_output = "C:/Users/Jugal/Desktop/TIME TABLE_new.jpeg"
   
    #------------Docx to Pdf Conversion-----------#
    convert(doc_path,pdf_output)
    #-------------PDF to Image Conversion----------------#
    images = convert_from_path(pdf_output)
   
    for image in images:
         print(Date)
         image_path = image.save(f"{doc_path}.jpg","JPEG")
         image_path = image.save(f"{Date}.jpg","JPEG")
         # Specify the path to your image file
         
         # Set the wallpaper using the specified image
         set_wallpaper(f'{doc_path}.jpg')
         os.remove(f'{doc_path}.jpg')
         os.remove(pdf_output)

init()

     
     
     
    
   
     


