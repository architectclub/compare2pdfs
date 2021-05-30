import difflib

text1 = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla cnt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,"
text2 = "HiLorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean cursus nunc,"

first_file = "myfile1.txt"
second_file = "myfile2.txt"

#create a text file
f = open(first_file, "w+")
f.write(text1)
f.close()
#sleep (5)
f = open(second_file, "w+")
f.write(text2)
f.close()

# first_file_lines = open(first_file).readlines()
# second_file_lines = open(second_file).readlines()

# difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines,
#                                           first_file, second_file)
# difference_report = open('diff_report.html', 'w')
# difference_report.write(difference)
# difference_report.close()


first_file_lines = open(first_file, 'r', encoding='utf-8').readlines()
second_file_lines = open(second_file, 'r', encoding='utf-8').readlines()
difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file, second_file)
difference_report = open('pdf_report.html', 'w', encoding='utf-8')
difference_report.write(difference)
difference_report.close()