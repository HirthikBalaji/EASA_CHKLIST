import pickle
import ollama
import chromadb

client = chromadb.PersistentClient(path="./")
collection = client.get_collection(name="EASA")


def create_rag(file):
    with open(f"./Extracted_Data/{file}.bin", "rb") as file:
        data = pickle.load(file)
        for id, pages in data.items():
            for page in pages:
                print(page['page_number'])
                response = ollama.embeddings(model="nomic-embed-text", prompt=page['text'])
                embedding = response["embedding"]
                collection.add(
                    ids=[str(page['page_number'])],
                    embeddings=[embedding],
                    documents=[page['text']]
                )


with open('chklist.data') as cklist:
    checklists = cklist.readlines()
counter = 1
for checklist in checklists:
    # create_rag("EASA_Concept_Paper_Guidance_for_Level_1and2_machine_learning_applications_Issue_02.pdf")
    with open('PROMPT.MD') as file:
        PROMPT = file.read()
    PROMPT = PROMPT.replace("<req>", checklist)
    # prompt = """Objective DA-02: Based on (sub)system requirements allocated to the AI/ML  constituent, the applicant should capture the following minimum for the AI/ML constituent req uirements: — safety requirements allocated to the AI/ML constituent (e.g. performance, reliability, resilience); — information security requirements allocated to the AI/ML constituent; — functional requirements allocated to the AI/ML constituent; — operational requirements allocated to the AI/ML constituent, including AI/ ML constituent ODD monitoring and performance monitoring (to support related objectives in Section C.3.2.6), detection of OoD input data and data-recordi ng requirements (to support objectives in Section C.3.2.7); — other non-functional requirements allocated to the AI/ML constituent (e.g.  scalability); and — interface requirements.
    # DEVELOP A CHECKLIST FOR CHECKING WHETHER THE ABOVE REQUIREMENT(S) ARE SATISFIED OR NOT. """
    response = ollama.embeddings(
        prompt=PROMPT,
        model="nomic-embed-text"
    )
    results = collection.query(
        query_embeddings=[response["embedding"]],
        n_results=4
    )
    data = ''
    for i in results['documents'][0]:
        data = data + "\n--\n" + i.replace("\n", '')
    # print(data)
    prompt = PROMPT.replace("<ref>", data)
    # print(f"{prompt}\n\n## OUTPUT:\n\n")
    output = ollama.generate(
        model="llama3",
        prompt=prompt,
        stream=True
    )
    o = ''
    for i in output:
        # print(i['response'], end='', flush=True)
        o = o + i['response']
    # print()
    filename = checklist.split("**")[0]
    with open(f"./CHECKLISTS/{filename}.md", "w") as filemd:
        filemd.write(o)
    print(f"DONE {counter}/{len(checklists)} . {filename}...")
    counter += 1
