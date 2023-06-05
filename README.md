## Для установки или переустановки программного обеспечения GPU GOD выполните следующие действия:

1. Обновите Hive Os
2. Перейдите на страницу инструкции на нашем сайте:
   http://ggc.center/#/instruction
3. Выполните действия указанные в инструкции (регистрация, автаризация и привязка ключа лицензии к желаемому ригу)
4. Включите риг после выполнения пункта 2.
5. Для установки ПО введите команду в консоле вашего рига или в командной строке (Установка на чистый HIVE OS): 
```bash
cd /home/ && git clone https://github.com/skret002/hive-install-gpugod.git && cd hive-install-gpugod && sudo chmod ugo+x install.bin && ./install.bin && systemctl status fan && rm -r /home/hive-install-gpugod && sudo reboot
```
6. Для переустановки ПО на HIVE OS (ЕСЛИ ВЫ УЖЕ ИСПОЛЬЗУЕТЕ НАШЕ ПО) используйте эту команду
```bash
cd /home/ && rm -r onrig && rm -r *.sh  && git clone https://github.com/skret002/hive-install-gpugod.git && cd hive-install-gpugod && sudo chmod ugo+x install.bin && ./install.bin && systemctl status fan && rm -r /home/hive-install-gpugod && sudo reboot
```
