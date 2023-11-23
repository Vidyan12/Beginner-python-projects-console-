#use pip install wikipedia

import wikipedia as wiki


def get_wikipedia_info(topic):
    try:
        # Get search suggestions for the input topic
        search_results = wiki.search(topic)
        print("Search Suggestions:", search_results)

        # Get a suggested search term for the input topic
        suggested_term = wiki.suggest(topic)
        print("Suggested Term:", suggested_term)

        # Get the summary of the article about the topic
        summary = wiki.summary(topic)
        print("Summary:", summary)

        # Set the language to French and get the summary in French
        wiki.set_lang("fr")
        summary_french = wiki.summary(topic)
        print("Summary in French:", summary_french)

        # Change the language back to English
        wiki.set_lang("en")

        # Get information about the Wikipedia page
        page = wiki.page(topic)

        # Get the title of the article
        print("Title:", page.title)

        # Get the URL of the article
        print("URL:", page.url)

        # Get the first 300 characters of the full content of the article
        print("Content:", page.content[:300] + "...")

        # Get all the images in the article (if any)
        images = page.images
        if images:
            print("Images:", images)
        else:
            print("No images available for this topic.")

        # Get all the references used in the article (if any)
        links = page.links
        if links:
            print("Links:", links)
        else:
            print("No references (links) available for this topic.")

    except wiki.DisambiguationError as e:
        print("Disambiguation Error. Options:", e.options)
    except wiki.PageError as e:
        print("Page Error. Please check the topic and try again.")


if __name__ == "__main__":
    while True:
        # Input the topic of interest
        user_input = input("Enter the topic you want to search on Wikipedia (or 'exit' to quit): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting Wikipedia Scraper. Goodbye!")
            break

        # Call the function with user input
        get_wikipedia_info(user_input)
        print("\n" + "=" * 50 + "\n")  # Add a separator for better readability


