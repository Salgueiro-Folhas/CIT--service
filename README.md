# CIT--service(ライブカメラの画像をGET(DoS)をする)

## 勉強のためにマルチプロセスを導入
勉強のためマルチプロセス実行を導入して記述した.<br>
(マルチプロセスが発揮されるほどの処理負荷ではない.)<br>
マルチプロセスで動作する記述は以下の通り.<br>
executor.submit()の()内がマルチプロセスで実行される.
```:Python3
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=3) as executor:
    executor.submit(GET_Narashino1)
    executor.submit(GET_Narashino2)
    executor.submit(GET_Tsudanuma)
```

またマルチスレッドで動作する記述は以下の通り.<br>
```:Python3
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit()
    executor.submit()
    executor.submit()
```