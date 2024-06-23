from listaEncadeada import DoublyLinkedListIterator
from livro import Livro
from Status import Status
from usuario import Usuario
from fila import ArrayQueue

class LibraryCatalog:
    def __init__(self):
        # Inicializa a lista encadeada para armazenar os livros
        self.livro_list = DoublyLinkedListIterator()

    def add_livro(self, livro):
        # Adiciona um livro à lista encadeada
        self.livro_list.addNode(livro)

    def iterator(self):
        # Retorna um iterador sobre a lista encadeada de livros
        return self.livro_list

    def __iter__(self):
        # Itera sobre os livros na lista encadeada
        current_node = self.livro_list.first_Node()
        while current_node:
            yield current_node.data
            current_node = current_node.nextNode

    def get_books(self):
        # Retorna uma lista de todos os livros no catálogo
        book_list = []
        current_node = self.livro_list.first_Node()
        while current_node:
            book_list.append(current_node.data)
            current_node = current_node.nextNode
        return book_list

# Função para corrigir os anos de publicação dos livros no catálogo
def converterDataAc(catalog):
    for livro in catalog:
        if len(livro['year']) > 4:
            primeiraLetra = int(livro['year'][0])
            ano = str((int(primeiraLetra) * -100) - 1000)
            livro['year'] = ano
        else:
            livro['year'] = str(int(livro['year']))
    return catalog

# Função para carregar o catálogo com uma fila de espera para cada livro
def load_catalog(books, catalog):
    print('Carregando o catálogo...')
    for title, author, year, publisher in books:
        # Cria um novo livro e adiciona ao catálogo
        novo_livro = Livro(None, title, author, year, publisher, Status.ATIVO)
        catalog.add_livro(novo_livro)
        # Adiciona uma fila de espera vazia para o novo livro
        novo_livro.reserve_queue = ArrayQueue()
        # Preenche a fila de espera com 10 usuários fictícios
        for i in range(10):
            novo_livro.reserve_queue.enqueue(Usuario(f"Usuário {i+1}"))

    # Adiciona índices aos livros
    adicionarIndiceAosLivros(catalog)
    return catalog

# Função para adicionar índices aos livros no catálogo
def adicionarIndiceAosLivros(catalog):
    index = 1
    current_node = catalog.livro_list.first_Node()
    while current_node:
        if current_node.data:
            current_node.data.id = index
            index += 1
            print('current_node.data.id', current_node.data.id)
            print('current_node.data.title', current_node.data.title)
        current_node = current_node.nextNode

# Código para carregar o catálogo quando este arquivo for importado
# Código para carregar o catálogo quando este arquivo for importado
livros = [
        ("A Casa dos Espíritos", "Isabel Allende", 1982, "Publisher A"),
        ("A Sangue Frio", "Truman Capote", 1966, "Publisher B"),
        ("A Hora da Estrela", "Clarice Lispector", 1977, "Publisher C"),
        ("A Revolução dos Bichos", "George Orwell", 1945, "Publisher D"),
        ("As Vinhas da Ira", "John Steinbeck", 1939, "Publisher E"),
        ("A Insustentável Leveza do Ser", "Milan Kundera", 1984, "Publisher F"),
        ("A Menina que Roubava Livros", "Markus Zusak", 2005, "Publisher G"),
        ("Alice no País das Maravilhas", "Lewis Carroll", 1865, "Publisher H"),
        ("A Abolição do Homem", "C.S. Lewis", 1943, "Publisher I"),
        ("Anna Karenina", "Liev Tolstói", 1877, "Publisher FW"),
        ("Brida", "Paulo Coelho", 1990, "Publisher J"),
        ("Bom Dia Camaradas", "Ondjaki", 2001, "Publisher K"),
        ("Branca de Neve", "Irmãos Grimm", 1812, "Publisher L"),
        ("Beloved", "Toni Morrison", 1987, "Publisher M"),
        ("Bartleby o Escrivão", "Herman Melville", 1853, "Publisher N"),
        ("Beowulf", "Autor Anônimo", 1000, "Publisher O"),
        ("Brooklyn", "Colm Tóibín", 2009, "Publisher P"),
        ("Bleak House", "Charles Dickens", 1852, "Publisher Q"),
        ("Black Leopard Red Wolf", "Marlon James", 2019, "Publisher R"),
        ("Brave New World", "Aldous Huxley", 1932, "Publisher FX"),
        ("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "Publisher S"),
        ("Crime e Castigo", "Fiódor Dostoiévski", 1866, "Publisher T"),
        ("O Coração das Trevas", "Joseph Conrad", 1899, "Publisher U"),
        ("O Complexo de Portnoy", "Philip Roth", 1969, "Publisher V"),
        ("Cidade de Deus", "Paulo Lins", 1997, "Publisher W"),
        ("Crepúsculo", "Stephenie Meyer", 2005, "Publisher X"),
        ("Código Da Vinci", "Dan Brown", 2003, "Publisher Y"),
        ("Crónica de uma Morte Anunciada", "Gabriel García Márquez", 1981, "Publisher Z"),
        ("Caninos Brancos", "Jack London", 1906, "Publisher AA"),
        ("Cristianismo Puro e Simples", "C.S. Lewis", 1952, "Publisher FY"),
        ("Dom Quixote", "Miguel de Cervantes", 1605, "Publisher A"),
        ("Diário de Anne Frank", "Anne Frank", 1947, "Publisher B"),
        ("Duna", "Frank Herbert", 1965, "Publisher C"),
        ("Drácula", "Bram Stoker", 1897, "Publisher D"),
        ("Doze Homens e Uma Sentença", "Reginald Rose", 1954, "Publisher E"),
        ("Doutor Jivago", "Boris Pasternak", 1957, "Publisher F"),
        ("David Copperfield", "Charles Dickens", 1850, "Publisher G"),
        ("Divergente", "Veronica Roth", 2011, "Publisher H"),
        ("Dias de Abandono", "Elena Ferrante", 2002, "Publisher I"),
        ("Death of a Salesman", "Arthur Miller", 1949, "Publisher FZ"),
        ("Em Busca do Tempo Perdido", "Marcel Proust", 1913, "Publisher J"),
        ("Eragon", "Christopher Paolini", 2002, "Publisher K"),
        ("East of Eden", "John Steinbeck", 1952, "Publisher GA"),
        ("Eva Luna", "Isabel Allende", 1987, "Publisher M"),
        ("Estação Onze", "Emily St. John Mandel", 2014, "Publisher N"),
        ("Escrava Isaura", "Bernardo Guimarães", 1875, "Publisher O"),
        ("Extraordinário", "R.J. Palacio", 2012, "Publisher P"),
        ("Era uma Vez no Oeste", "Sergio Leone", 1968, "Publisher Q"),
        ("Esperança", "Suzanne Collins", 2010, "Publisher R"),
        ("Ender's Game", "Orson Scott Card", 1985, "Publisher GB"),
        ("Frankenstein", "Mary Shelley", 1818, "Publisher S"),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Publisher T"),
        ("Felicidade Clandestina", "Clarice Lispector", 1971, "Publisher U"),
        ("Filhos do Éden: Herdeiros de Atlântida", "Eduardo Spohr", 2018, "Publisher V"),
        ("Flores para Algernon", "Daniel Keyes", 1959, "Publisher W"),
        ("Fale!", "Laurie Halse Anderson", 1999, "Publisher X"),
        ("Fique Comigo", "Ayobami Adebayo", 2017, "Publisher Y"),
        ("Família", "J. California Cooper", 1991, "Publisher Z"),
        ("Fogo e Sangue", "George R.R. Martin", 2018, "Publisher AA"),
        ("Fala Sério Mãe", "Thalita Rebouças", 2008, "Publisher GC"),
        ("Grande Sertão: Veredas", "João Guimarães Rosa", 1956, "Publisher AB"),
        ("Guerra e Paz", "Liev Tolstói", 1869, "Publisher AC"),
        ("Gregor - Underland Chronicles", "Suzanne Collins", 2003, "Publisher GF"),
        ("Garota Interrompida", "Susanna Kaysen", 1993, "Publisher AE"),
        ("Garota Exemplar", "Gillian Flynn", 2012, "Publisher AF"),
        ("Germinal", "Émile Zola", 1885, "Publisher GG"),
        ("Gente Pobre", "Fiódor Dostoiévski", 1846, "Publisher AH"),
        ("Game of Thrones", "George R. R. Martin", 1996, "Publisher GE"),
        ("Geração de Valor", "Flávio Augusto da Silva", 2013, "Publisher AJ"),
        ("Gone with the Wind", "Margaret Mitchell", 1936, "Publisher GD"),
        ("Hamlet", "William Shakespeare", 1603, "Publisher AK"),
        ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "Publisher AL"),
        ("Homo Deus", "Yuval Noah Harari", 2015, "Publisher AM"),
        ("Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "Publisher AN"),
        ("Hércules", "Bernard Evslin", 1964, "Publisher AO"),
        ("Histórias Extraordinárias", "Edgar Allan Poe", 1839, "Publisher AP"),
        ("História de Duas Cidades", "Charles Dickens", 1859, "Publisher AQ"),
        ("Homo Sapiens", "Yuval Noah Harari", 2011, "Publisher AR"),
        ("Hunger Games", "Suzanne Collins", 2008, "Publisher AS"),
        ("Halo: The Fall of Reach", "Eric Nylund", 2001, "Publisher GH"),
        ("It - A Coisa", "Stephen King", 1986, "Publisher AT"),
        ("Into the Wild", "Jon Krakauer", 1996, "Publisher AU"),
        ("Inferno", "Dan Brown", 2013, "Publisher AV"),
        ("O Iluminado", "Stephen King", 1977, "Publisher AW"),
        ("In Cold Blood", "Truman Capote", 1966, "Publisher AX"),
        ("Ísis Sem Véu", "Helena Blavatsky", 1877, "Publisher AY"),
        ("Inferno", "Dante Alighieri", 1320, "Publisher AZ"),
        ("Irmãos Karamazov", "Fiódor Dostoiévski", 1880, "Publisher BA"),
        ("Irmãos de Sangue", "Nora Roberts", 2006, "Publisher BB"),
        ("Insurgente", "Veronica Roth", 2012, "Publisher GI"),
        ("Jane Eyre", "Charlotte Brontë", 1847, "Publisher BC"),
        ("Jogos Vorazes", "Suzanne Collins", 2008, "Publisher BD"),
        ("Jogador Nº 1", "Ernest Cline", 2011, "Publisher BE"),
        ("Judas", "Amós Oz", 2014, "Publisher BF"),
        ("Julius Caesar", "William Shakespeare", 1599, "Publisher BG"),
        ("Jurassic Park", "Michael Crichton", 1990, "Publisher BH"),
        ("João e Maria", "Irmãos Grimm", 1812, "Publisher BI"),
        ("Jonathan Strange & Mr. Norrell", "Susanna Clarke", 2004, "Publisher BJ"),
        ("Jack o Estripador", "Kerri Maniscalco", 2016, "Publisher BK"),
        ("Julieta Imortal", "Stacey Jay", 2011, "Publisher GJ"),
        ("Kafka à Beira-Mar", "Haruki Murakami", 2002, "Publisher BL"),
        ("Kairós", "Padre Marcelo Rossi", 2013, "Publisher BM"),
        ("King Kong Theory", "Virginie Despentes", 2006, "Publisher BN"),
        ("Kitchen Confidential", "Anthony Bourdain", 2000, "Publisher BO"),
        ("Kama Sutra de Grey", "Mallanaga Vatsyayana", 2012, "Publisher BP"),
        ("Killing Commendatore", "Haruki Murakami", 2017, "Publisher BQ"),
        ("Klara and the Sun", "Kazuo Ishiguro", 2021, "Publisher BR"),
        ("Kiss the Girls", "James Patterson", 1995, "Publisher BS"),
        ("Kane and Abel", "Jeffrey Archer", 1979, "Publisher BT"),
        ("Kidnapped", "Robert Louis Stevenson", 1886, "Editora GK"),
        ("Lolita", "Vladimir Nabokov", 1955, "Publisher BU"),
        ("Laranja Mecânica", "Anthony Burgess", 1962, "Publisher BV"),
        ("Lua Azul", "Alyson Noël", 2009, "Publisher BW"),
        ("Lisbela e o Prisioneiro", "Osman Lins", 1961, "Publisher BX"),
        ("Lavoura Arcaica", "Raduan Nassar", 1975, "Publisher BY"),
        ("Lua Nova", "Stephenie Meyer", 2006, "Publisher BZ"),
        ("Laços de Família", "Clarice Lispector", 1960, "Publisher CA"),
        ("Les Misérables", "Victor Hugo", 1862, "Publisher CB"),
        ("La Casa de Papel", "Arthur Harari", 2017, "Publisher CC"),
        ("Louco aos Poucos", "Felipe Rocha", 2017, "Publisher GL"),
        ("Moby Dick", "Herman Melville", 1851, "Publisher BD"),
        ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, "Publisher BE"),
        ("Macunaíma", "Mário de Andrade", 1928, "Publisher BF"),
        ("Matilda", "Roald Dahl", 1988, "Publisher BG"),
        ("Macbeth", "William Shakespeare", 1623, "Publisher BH"),
        ("Mistborn: The Final Empire", "Brandon Sanderson", 2006, "Publisher BI"),
        ("Maus", "Art Spiegelman", 1980, "Publisher BJ"),
        ("Maus: A Survivor's Tale", "Art Spiegelman", 1986, "Publisher BK"),
        ("Middlemarch", "George Eliot", 1871, "Publisher BL"),
        ("Madwand", "Roger Zelazny", 1981, "Publisher GM"),
        ("Night in the Country", "Cynthia Rylant", 1998, "Publisher BM"),
        ("Norwegian Wood", "Haruki Murakami", 1987, "Publisher BN"),
        ("Neuromancer", "William Gibson", 1984, "Publisher BO"),
        ("Nome do Vento", "Patrick Rothfuss", 2007, "Publisher BP"),
        ("Na Natureza Selvagem", "Jon Krakauer", 1996, "Publisher BQ"),
        ("Night", "Elie Wiesel", 1956, "Publisher BR"),
        ("Never Let Me Go", "Kazuo Ishiguro", 2005, "Publisher BS"),
        ("Nada", "Carmen Laforet", 1944, "Publisher BT"),
        ("Nossa Senhora de Paris", "Victor Hugo", 1831, "Publisher BU"),
        ("Nation", "Terry Pratchett", 2008, "Publisher GN"),
        ("O Apanhador no Campo de Centeio", "J.D. Salinger", 1951, "Publisher BV"),
        ("O Velho e o Mar", "Ernest Hemingway", 1952, "Publisher BW"),
        ("O Hobbit", "J.R.R. Tolkien", 1937, "Publisher BX"),
        ("Os Miseráveis", "Victor Hugo", 1862, "Publisher BY"),
        ("Orgulho e Preconceito", "Jane Austen", 1813, "Publisher BZ"),
        ("O Primo Basílio", "José Maria de Eça de Queirós", 1878, "Publisher CA"),
        ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Publisher CB"),
        ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Publisher CC"),
        ("O Sol é para Todos", "Harper Lee", 1960, "Publisher CD"),
        ("O Exorcista", "William Peter Blatty", 1971, "Publisher L"),
        ("Percy Jackson e o Ladrão de Raios", "Rick Riordan", 2005, "Publisher CE"),
        ("Pollyanna", "Eleanor H. Porter", 1913, "Publisher CF"),
        ("Pippi Meialonga", "Astrid Lindgren", 1945, "Publisher CG"),
        ("Peter Pan", "J.M. Barrie", 1911, "Publisher CH"),
        ("Pensar Rápido Pensar Devagar", "Daniel Kahneman", 2011, "Publisher CI"),
        ("Ponto de Impacto", "Dan Brown", 2001, "Publisher CJ"),
        ("Pele de Asno", "Charles Perrault", 1694, "Publisher CK"),
        ("Pride and Prejudice", "Jane Austen", 1813, "Publisher CL"),
        ("Persuasion", "Jane Austen", 1817, "Publisher CM"),
        ("Paddington", "Michael Bond", 1958, "Publisher GP"),
        ("Quincas Borba", "Machado de Assis", 1891, "Publisher CN"),
        ("Quem Mexeu no Meu Queijo?", "Spencer Johnson", 1998, "Publisher CO"),
        ("Quem É Você Alasca?", "John Green", 2005, "Publisher CP"),
        ("Quando Nietzsche Chorou", "Irvin D. Yalom", 1992, "Publisher CQ"),
        ("Querido John", "Nicholas Sparks", 2006, "Publisher CR"),
        ("Que Esperar Quando Você Está Esperando", "Heidi Murkoff", 1984, "Publisher CS"),
        ("Quem Mexeu na Minha Emoção?", "Ken Blanchard", 2001, "Publisher CT"),
        ("Querido Diário Otário", "Jim Benton", 1998, "Publisher CU"),
        ("Quem Pensa Enriquece", "Napoleon Hill", 1937, "Publisher CV"),
        ("Queenie", "Candice Carty-Williams", 2019, "Publisher GQ"),
        ("Romeu e Julieta", "William Shakespeare", 1597, "Publisher CW"),
        ("Razão e Sensibilidade", "Jane Austen", 1811, "Publisher CX"),
        ("Rumo ao Farol", "Virginia Woolf", 1927, "Publisher CY"),
        ("Ratos e Homens", "John Steinbeck", 1937, "Publisher CZ"),
        ("Revolução dos Bichos", "George Orwell", 1945, "Publisher DA"),
        ("Rouxinol", "Kristin Hannah", 2015, "Publisher DB"),
        ("Romeu Julieta e Cia", "William Shakespeare", 1662, "Publisher DC"),
        ("Robinson Crusoé", "Daniel Defoe", 1719, "Publisher DD"),
        ("Rumo à Estação Finlandia", "Edmund Wilson", 1940, "Publisher DE"),
        ("Rebecca", "Daphne du Maurier", 1938, "Publisher GR"),
        ("Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", 2014, "Publisher DF"),
        ("Sob o Sol da Toscana", "Frances Mayes", 1996, "Publisher DG"),
        ("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2014, "Publisher DH"),
        ("Se Eu Ficar", "Gayle Forman", 2009, "Publisher DI"),
        ("Silmarillion", "J.R.R. Tolkien", 1977, "Publisher DJ"),
        ("Sobrevivendo entre Lobos", "Misha Defonseca", 1997, "Publisher DK"),
        ("Stargirl", "Jerry Spinelli", 2000, "Publisher DL"),
        ("Saudades do Brasil", "Sérgio Buarque de Holanda", 1930, "Publisher DM"),
        ("Silêncio dos Inocentes", "Thomas Harris", 1988, "Publisher DN"),
        ("Sonhos de Uma Noite de Verão", "William Shakespeare", 1600, "Publisher DO"),
        ("Sussurro", "Becca Fitzpatrick", 2009, "Publisher DP"),
        ("Sob a Redoma", "Stephen King", 2009, "Publisher DQ"),
        ("Sherlock Holmes", "Arthur Conan Doyle", 1887, "Publisher DR"),
        ("Sob a Redoma", "Stephen King", 2009, "Publisher DS"),
        ("Sob a Redoma", "Stephen King", 2009, "Publisher DT"),
        ("Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, "Publisher DU"),
        ("Sherlock Holmes", "Arthur Conan Doyle", 1892, "Publisher DV"),
        ("Sob a Redoma", "Stephen King", 2009, "Publisher DW"),
        ("Stoner", "John Williams", 1965, "Publisher DL"),
        ("Silêncio dos Inocentes", "Thomas Harris", 1988, "Publisher DM"),
        ("Silmarillion", "J.R.R. Tolkien", 1977, "Publisher DN"),
        ("Shiver", "Maggie Stiefvater", 2009, "Publisher GS"),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Publisher DO"),
        ("Tess dos d'Urbervilles", "Thomas Hardy", 1891, "Publisher DP"),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Publisher DQ"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Publisher DR"),
        ("The Da Vinci Code", "Dan Brown", 2003, "Publisher DS"),
        ("The Shining", "Stephen King", 1977, "Publisher DT"),
        ("The Stand", "Stephen King", 1978, "Publisher DU"),
        ("The Book Thief", "Markus Zusak", 2005, "Publisher DV"),
        ("The Outsider", "Stephen King", 2018, "Publisher DW"),
        ("The Idiot", "Fiódor Dostoiévski", 1869, "Publisher GT"),
        ("Ulysses", "James Joyce", 1922, "Publisher DX"),
        ("Um Estudo em Vermelho", "Arthur Conan Doyle", 1887, "Publisher DY"),
        ("Um Conto de Duas Cidades", "Charles Dickens", 1859, "Publisher DZ"),
        ("Um Estranho no Ninho", "Ken Kesey", 1962, "Publisher EA"),
        ("Um Mar de Rosas", "Nora Roberts", 1999, "Publisher EB"),
        ("Uma Breve História do Tempo", "Stephen Hawking", 1988, "Publisher EC"),
        ("Um Lugar Bem Longe Daqui", "Delia Owens", 2018, "Publisher ED"),
        ("Um Copo de Cólera", "Raduan Nassar", 1978, "Publisher EE"),
        ("Um Dia", "David Nicholls", 2009, "Publisher EF"),
        ("Unbroken", "Laura Hillenbrand", 2010, "Publisher GU"),
        ("Viagem ao Centro da Terra", "Júlio Verne", 1864, "Publisher EG"),
        ("Vidas Secas", "Graciliano Ramos", 1938, "Publisher EH"),
        ("Vinte Mil Léguas Submarinas", "Júlio Verne", 1870, "Publisher EI"),
        ("Vá Coloque um Vigia", "Harper Lee", 2015, "Publisher EJ"),
        ("Veronika Decide Morrer", "Paulo Coelho", 1998, "Publisher EK"),
        ("Vermelho Como o Sangue", "Salla Simukka", 2013, "Publisher EL"),
        ("Viva o Povo Brasileiro", "João Ubaldo Ribeiro", 1984, "Publisher EM"),
        ("Vingança", "Nora Roberts", 2006, "Publisher EN"),
        ("Vozes de Tchernóbil", "Svetlana Alexievich", 1997, "Publisher EO"),
        ("Valentine's", "Elizabeth Wetmore", 2020, "Publisher GV"),
        ("Walden", "Henry David Thoreau", 1854, "Publisher EP"),
        ("Watchmen", "Alan Moore", 1986, "Publisher EQ"),
        ("We Need to Talk About Kevin", "Lionel Shriver", 2003, "Publisher ER"),
        ("Waiting for Godot", "Samuel Beckett", 1953, "Publisher ES"),
        ("White Teeth", "Zadie Smith", 2000, "Publisher ET"),
        ("Water for Elephants", "Sara Gruen", 2006, "Publisher EU"),
        ("Wuthering Heights", "Emily Brontë", 1847, "Publisher EV"),
        ("Winter Garden", "Kristin Hannah", 2010, "Publisher EW"),
        ("Wait Until the Evening", "Hal Bennett", 1974, "Publisher GW"),
        ("Waiting for Godot", "Samuel Beckett", 1952, "Publisher HW"),
        ("X-Men: Dias de um Futuro Esquecido", "Chris Claremont", 1981, "Publisher EX"),
        ("X-Men: Inferno", "Chris Claremont", 1988, "Publisher EY"),
        ("X-Men: A Saga da Fênix Negra", "Chris Claremont", 1980, "Publisher EZ"),
        ("X-Men: A Queda dos Mutantes", "Chris Claremont", 1986, "Publisher FA"),
        ("X-Men: Deus Ama o Homem Mata", "Chris Claremont", 1982, "Publisher FB"),
        ("X-Men: Era do Apocalipse", "Scott Lobdell", 1995, "Publisher FC"),
        ("X-Men: Império Secreto", "Chris Claremont", 1987, "Publisher FD"),
        ("X-Men: Fênix", "Chris Claremont", 1976, "Publisher FE"),
        ("X-Men: Fênix Negra", "Chris Claremont", 1980, "Publisher GX"),
        ("You", "Caroline Kepnes", 2014, "Publisher FF"),
        ("Yellow Crocus", "Laila Ibrahim", 2011, "Publisher FG"),
        ("Year of Yes", "Shonda Rhimes", 2015, "Publisher FH"),
        ("Yoga for Life", "Colleen Saidman Yee", 2009, "Publisher FI"),
        ("Yoga Anatomy", "Leslie Kaminoff", 2007, "Publisher FJ"),
        ("Yoga Girl", "Rachel Brathen", 2015, "Publisher FK"),
        ("You Are a Badass", "Jen Sincero", 2013, "Publisher FL"),
        ("Yoga Mind Body & Spirit", "Donna Farhi", 2000, "Publisher FM"),
        ("Year of Wonders", "Geraldine Brooks", 2001, "Publisher GY"),
        ("Yiddish for Pirates", "Gary Barwin", 2016, "Publisher HY"),
        ("Zorba o Grego", "Nikos Kazantzakis", 1946, "Publisher FN"),
        ("Zona Morta", "Stephen King", 1979, "Publisher FO"),
        ("Zero", "Ignácio de Loyola Brandão", 1974, "Publisher FP"),
        ("Zen e a Arte da Manutenção de Motocicletas", "Robert M. Pirsig", 1974, "Publisher FQ"),
        ("Zodíaco", "Robert Graysmith", 1986, "Publisher FR"),
        ("Zealot", "Reza Aslan", 2013, "Publisher FS"),
        ("Zorba o Grego", "Nikos Kazantzakis", 1946, "Publisher FT"),
        ("Zumbis vs Unicórnios", "Meg Cabot & Holly Black", 2010, "Publisher FU"),
        ("Z: A Novel of Zelda Fitzgerald", "Therese Fowler", 2013, "Publisher GZ"),
        ("Zel", "Donna Jo Napoli", 1996, "Publisher HZ")
]

# Instancia o catálogo
catalog = LibraryCatalog()
# Carrega o catálogo com os livros e suas filas de espera
load_catalog(livros, catalog)
