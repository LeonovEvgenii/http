Файл p2p_http является элементом p2p сети роботов.
При запуске, смотрит карту сети в виде списка хостов и отправляет им гет запросы.
При получении ответа смотрит свой файл и сравнивает с ответом.
Если замечена разница, то новые данные добавляются к себе в файл в виде json.
Файл запускается с параметрами порта с которого он работет и именем файла, кда складываются данные.
Возможно обращение к самому себе.