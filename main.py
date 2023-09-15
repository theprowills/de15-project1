from modules.library_item import LibraryItem

item = LibraryItem('judul 1', None, 'deskripsi judul 1')

# print(item.title)
# print(item.upc)
# print(item.subject)


from modules.book import Book
item = Book('isbn', 'authors', 'title', 'subject', 'dds_number', 'upc')
# print(item.isbn)


from modules.magazine import Magazine
magazine = Magazine('title magazine', 'upc', 'subject', 'volume', 'issue')
# print(magazine.title)

from modules.cd import Cd
cd = Cd('title', 'upc', 'subject', 'artist')
# print(cd.title)


from modules.dvd import Dvd
dvd = Dvd('titlle dvd', 'upc', 'subject', 'actors', 'directors', 'genre')
# print(dvd.title)



from modules.catalog import Catalog
#input_search = 'test'
#results = Catalog(None).search('test')


import json
f = open('files/data.json')

data_json = json.load(f)

list_book = []
list_magazine = []
list_dvd = []
list_cd = []

for item in data_json:
    if item['source'] == 'book':
        list_book.append(
            Book(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                isbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )
    elif item['source'] == 'magazine':
        list_magazine.append(
            Magazine(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                volume=item['volume'],
                issue=item['issue']
            )
        )
    elif item['source'] == 'cd':
        list_cd.append(
            Cd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                artist=item['artist']
            )
        )
    elif item['source'] == 'dvd':
        list_dvd.append(
            Dvd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                actors=item['actors'],
                directors=item['directors'],
                genre=item['genre']
            )
        )
                
                           
# print(list_book)
# print(list_magazine)

catalog_all = [list_book, list_magazine, list_dvd, list_cd]

input_search = 'media_cnn'
results = Catalog(catalog_all).search(input_search)

print('=====| results |======')
for index, result in enumerate(results):
    print({f'result ke-{index+1} | {result}'})

