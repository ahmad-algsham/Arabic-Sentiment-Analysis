
import regexarabic as ra

text = 'الان بالَعربي @شمس_انت 2و @شمس8انا وأاإ ىئ @_شمس @ - 5وبالهاششششتاق👍 ذالك هذه الىى علييي AbTihal ): #نحن_بالعربيه ' \
       '45ؤ #نحن2انت و ' \
       ' #نحن_فيك ' \
       'https://www.githup.com       '

cln = ra.remove(text)
cln = ra.harakat(cln)
cln = ra.WordsFiltires(cln)

print(cln)
