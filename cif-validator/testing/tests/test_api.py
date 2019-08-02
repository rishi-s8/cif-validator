import pytest
import requests

url = 'http://127.0.0.1:8091/compute'

def test_index():
    r = requests.get(url+'/')
    assert r.status_code == 200

def test_validate():
    upload = {'cif': open('tests/valid_1.cif', 'rb')}
    response = requests.post(url+'/validate', files=upload)
    assert response.status_code == 200
    assert response.json()['status'] == 'valid'

    upload = {'cif': open('tests/valid_2.cif', 'rb')}
    response = requests.post(url+'/validate', files=upload)
    assert response.status_code == 200
    assert response.json()['status'] == 'valid'

    upload = {'cif': open('tests/valid_3.cif', 'rb')}
    response = requests.post(url+'/validate', files=upload)
    assert response.status_code == 200
    assert response.json()['status'] == 'valid'
    
    upload = {'cif': open('tests/valid_4.cif', 'rb')}
    response = requests.post(url+'/validate', files=upload)
    assert response.status_code == 200
    assert response.json()['status'] == 'valid'

    upload = {'cif': open('tests/invalid_1.cif', 'rb')}
    response = requests.post(url+'/validate', files=upload)
    assert response.status_code == 200
    assert response.json()['status'] == 'error'

    upload = {'cif': open('tests/invalid_2.cif', 'rb')}
    response = requests.post(url+'/validate', files=upload)
    assert response.status_code == 200
    assert response.json()['status'] == 'error'