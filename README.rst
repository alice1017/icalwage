What's icalwage?
###################

**icalwage** はMacOSで標準搭載されている **iCal** というアプリケーションで書き出された **.ics** ファイルを指定して、
(アルバイトの)時給計算をするスクリプトです。

このicalwageを使うには予めiCalでカレンダーを.icsファイルとして書き出す必要がありますが、ここでは説明しませんので以下のURLを参考にしてください。

*iCalの予定をGoogleカレンダーへ移動する方法(http://d.hatena.ne.jp/sho_oza/20120417/1334674583)*

Usage
########

::

    $ icalwage.py [OPTIONS]
    ------------------------------
    OPTIONS :
    -s, --show-event [[ics_file]]
    Show event list and time. Please set .ics file to arg.

    -w, --work-wage [[ics_file], [hourly_wage]]
    Calcuation your wage. Please set ics file and hourly wage

    -c, --csv [[ics_file], [filename]]
    Make CSV file. Please set ics file and file name.

    -h, --help, help
    Show this usage message.


How to use
############

-s, --show-event [ics_file_path]
    icsファイルに含まれているイベントを出力します。
    出力形式は  このような形式です。

    ::

        2012/11/19 : 08:30:00 ~ 17:00:00 : 8時間 30分

-w --work-wage [ics_file_path], [hourly_wage]
    :hourly_wage: 時給単価
    icsファイルに含まれているイベントを解析して予想給料を出力します。

-c --csv [ics_file_path], [csv_file_name]
    icsファイルに含まれているイベントを解析してcsvファイルに出力します。

    
Copyright and License
########################

Copyright Alice1017 all rights reserved.

MIT license.
