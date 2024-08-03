Для запуска скрипта используйте терминал. 

Посредством pwd определите свою текущую директорию. Затем в эту папку скопируйте файл base_editors_selector.py.

После размещения файла в нужной папке скопируйте путь до этого файла использую контекстное меню.

Данные передаются программе через командную строку.

Для того чтобы запустить программу:
1) откройте терминал 
2) в командной строке введите python3 и путь до файла /Users/venefica/PycharmProjects/BEs/base_editors_selector.py через 1 пробел
3) последовательно вводите данные, которые запрашивает программа, и нажимайте Enter

Обратите внимание! Необходимо строго соблюдать порядок ввода данных в командной строке.

Порядок ввода данных:
1) 61-нуклеотидная последовательность дикого типа фланкирующая сайт мутации (регистр не важен);
2) нуклеотид (один знак) на который произошла замена в случае данного SNP;
3) название для документа в который программа сохранит результат с расширением
.fa (одной сторонкой без пробелов).

Пример данных для тестового запуска программы и передачи данных:
CCCGCCGCATCTCCTTCAGCGCGAGCCACCGATTGTACAGGTAGGGTGTGCACACAGGTAC
A
Base editors system file 001.fa

Выберите удобную для Вас директорию, куда будут записываться multy-FASTA файлы.
Обратите внимание! Если не прописывать новое имя файла (последнее слово перед расширением файла «.fa») при каждом запуске программы, файл будет перезаписываться под тем же именем вместо ранее созданного, что приведет к потере ранее полученных результатов.

Последовательность протоспейсера выводится в терминал.
