from preprocessing import *

if __name__ == "__main__":
    
    output = open("output.txt", "w+")
    document_set = get_set("news.csv")
    features_names = document_set.columns

    serie = document_set["title"]

    documents = document_set["title"]+" " +" "+document_set["description"]+" "+document_set["text"]
    
    print(documents)

    for doc in documents.items():
        title = doc[1]
        # description = doc[2]
        # text = doc[3]
        
        title_tokens = get_tokens(title)
        # desc_tokens = get_tokens(description)
        # text_tokens = get_tokens(text)

        print(title, file=output.encode("utf-8"))
        # print(title_tokens, file=output)


        # stop_words_dropped = drop_stop_words(tokens)
        # print(stop_words_dropped)
    
    # print(dir(tokens[0]))
    # for f in document_set:
        
    #     for index, value in serie:
    #         print(value.encode("utf-8"))



# "title": 'More vital now: Gay-straight alliances go virtual during coronavirus pandemic',
# "description": "Lily Overacker and Laurell Pallot start each gay-straight alliance meeting with everyone introducing themselves, saying their pronouns and sharing highs and lows of the week.",
# "text": "Lily Overacker and Laurell Pallot start each gay-straight alliance meeting with everyone introducing themselves, saying their pronouns and sharing highs and lows of the week. Except lately it's been through email chains instead of in-person for the Grade 12 students in Lacombe, Alta. Such school clubs are meant to provide safe spaces for LGBTQ students and their allies. Students, teachers and community groups are working to ensure that support is still available as the COVID-19 pandemic keeps kids out of school. ""It's definitely harder because you want to be able to see those people and be around them,"" said Overacker, 18. ""But I think we are making the best out of the situation that we can and focusing on making sure that kids still know that there's people there to support them."" Overacker and Pallot want to hold a virtual end-of-year celebration for LGBTQ students. ""We're thinking it'll be over Zoom and we want it to be Alberta-wide,"" said Pallot, 17. She said community groups could host multiple Zoom sessions simultaneously. ""We'll have a Zoom room with a DJ and dancing and games and just multiple different ones that kids can choose."" Gay-straight alliances are moving online, to ensure support is still available during the pandemic. (Tiphanie Roquette/Radio-Canada/CBC) Pallot said the virtual prom is a way of ""finding light in this situation,"" with the bonus of meeting new people before she goes away to college in the fall. Hilary Mutch, who co-ordinates a GSA network in southern Alberta through the Centre for Sexuality, said isolation is one of the biggest issues for LGBTQ youth at the best of times. ""As much as possible, it's so important to think 'what are the things that we're doing to combat those feelings of isolation, lack of resources, lack of supports that people might be feeling at home, especially if their home isn't affirming or respectful of their identity?""' School divisions have approached holding GSAs during the shutdown in different ways, whether it's through email, group chats, video conferencing or social media. The Arc Foundation, which runs a program called SOGI 123 to make schools more inclusive, recently held a webinar to help educators run virtual GSAs.  More people are experiencing negativity within their unsupportive households because they're there constantly,​​​​​​.- Mav Gilchrist, 17-year-old student Scout Gray, SOGI 123's leader, said 140 people signed up — mostly in British Columbia, but some in Alberta. ""Teachers are stretched real thin right now and they're taking the time to make sure these clubs are getting running, which shows that they're really dedicated and shows that there's a need."" Gray added it's important to coach youth on privacy. For instance, if teens don't want everyone to know they're part of a GSA, they would need to think about whether having their face shown in a video chat window beamed into someone else's home is a good idea. ""We want to make sure that ... they understand that things they put out on the internet could be recorded, could be used in other places,"" Gray said. If youth don't want their families knowing, they could participate by phone during a walk around the neighbourhood so no one overhears, Gray added. Mav Gilchrist, a 17-year-old Grade 12 student in St. Albert, Alta., has noticed some students choose their words carefully or mute their mics during their GSA's Google Meet chats. Gilchrist said efforts have been made to ensure names appearing in video chat windows reflect trans students' true gender identities, which isn't always the case when accounts are linked to school-issued email addresses. Gilchrist said not as many students have been participating as usual — possibly because of scheduling or unsupportive households. But Gilchrist said it's crucial the club keep going in some form. ""More people are experiencing negativity within their unsupportive households because they're there constantly,"" Gilchrist said. ""The support that GSAs provide was vital before — it is even more vital now."" Renee LeClerc, a teacher supervisor for Gilchrist's GSA at Paul Kane High School, said students use the time to talk about whatever they want — whether that be baking, TV shows or anime. ""We are very rarely focused on LGBTQ-specific issues for an entire meeting. It is almost always just things that teenagers talk about,"" she said. ""We all just want to be in a place where we see ourselves reflected and supported."""



