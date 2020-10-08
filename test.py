import requests
import time

be_url = "http://127.0.0.1:8000/{}/"
# be_url = "https://recruiting-api.augmented.globant.com/{}"
header = {'Accept': 'application/json'}
radar_url = "http://127.0.0.1:8007/{}"


# función para crear los archivos que se van a grabar en el bucket
def create_audio_file(path, file_size):
    f = open(path, 'wb')
    f.write(bytearray(file_size))
    f.close()
    f = open(path, 'rb')
    return f

def retrieve_image_file(path):
    f = open(path, 'rb')
        
    return f
    
    
if __name__ == '__main__':
    fp = create_audio_file('test.bin', 1000)
    fp = retrieve_image_file('/home/lmpizarro/Documents/foto_santander.JPG')
    
    url = be_url.format('uploadfile')
    response_audio = requests.post(url,
                                   files={'file': fp},
                                   # data=data_audio,
                                   headers=header)
    print('response_audio_json', response_audio.json())
