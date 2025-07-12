def city_country(city, country, population=None, language=None   ):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result +=f", {language.title()}"
    return result


if __name__ =='__main__':
    print(city_country("Dallas", "United States"))
    print(city_country("Mumbai", "India", "12.5 million "))
    print(city_country("Tokyo", "Japan", "37 million","Japanese"))
    