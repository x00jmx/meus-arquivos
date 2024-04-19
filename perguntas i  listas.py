perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Tinha dívidas com a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = [input(pergunta + " (s/n): ").lower() for pergunta in perguntas]

num_s = respostas.count("s")

if num_s == 2:
    print("Você é suspeito(a) do crime.")
elif 3 <= num_s <= 4:
    print("Você é cúmplice do crime.")
elif num_s == 5:
    print("Você é o principal suspeito(a) do crime.")
else:
    print("Você não é considerado(a) como suspeito(a) do crime.")