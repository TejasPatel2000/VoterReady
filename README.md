STAY INFORMED AND NOT MISINFORMED

About Us

Tejas Patel and Anuja Badeti are Juniors studying Computer Science at the New Jersey Institute of Technology. They are passionate about using technology to advance educational and political awareness, especially as the 2020 election approaches. Making informed decisions during this election is imperative to ensure the prosperity of the country and creating an application to help that mission is a goal of both of ours.

Problem

About six in ten Americans say too many uninformed people voting (60%) and media bias against certain candidates (57%) are major problems. Close to half (45%) of the public say outside influence or interference from foreign governments is a major problem. News has recently been revealed that The Russian government interfered in the 2016 U.S. presidential election with the goals of harming the campaign of Hillary Clinton, boosting the candidacy of Donald Trump, and increasing political and social discord in the United States. Being uninformed and misinformed are two issues that can be achieved by further research and fact checking.

Technology used

APIs: Sci-kit Learn, NLTK, Wikipedia, YoutubeTranscriptAPI | Languages: Python, CSS, Javascript, HTML | Full stack: Django

How It Works

Input: Youtube URL Derive video id to get the transcript of the video using Youtube’s API Create a vocabulary list that holds the top trending twitter words in the #2020elections Use Sklearn’s CountVectorizer to convert a collection of text documents to a matrix of token counts and obtain the most prevalent words in the given text. Compare the most prevalent words to the vocabulary list. The words that are in common will then be saved as keywords of the video. Using the keywords that were generated, input into Wikipedia’s API to get an article URL and Summary that related to the topic of the video. Using the vocabulary and keywords, find the phrase in the video transcript that has the most usages of the keywords. Repeat the last step with the Wikipedia article summary to get the phrase that includes the most usages of the keywords. After both sentences are obtained (from Wikipedia and from the video), run a mathematical method that tokenizes each word in the sentences to compute a similarity score between the two sentences. Output the similarity score and determine where the score falls in the threshold. If the score is less than 35% similar, notify the user that the video source is not reliable. If the score is between 35%-50%, notify the user that the video is possibly factual. If the score is over 50%, the video is most likely accurate information. In all cases, also provide a Wikipedia article that provides more information on the video contents to ensure that the user stays informed.

Further Implementations

Create a Google Chrome extension that allows a user to directly fact check and get further information while watching a youtube video Expand the project to be able to fact check any type of video and to get more information from articles outside of Wikipedia Be able to apply this application on live videos such as Presidential Debates

Desired Audience

Voters Anyone looking to stay informed and not be misinformed

Challenges

Generating the keywords for each video (Using twitter trending keywords)
