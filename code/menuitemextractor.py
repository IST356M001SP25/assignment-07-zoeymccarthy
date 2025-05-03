if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    price = price.replace("$", "")
    price = price.replace(",", "")
    return float(price)

def clean_scraped_text(scraped_text: str) -> list[str]:
    items = scraped_text.split("\n")
    cleaned = []
    for item in items:
        if len(item.strip()) == 0:
            continue
        if item in ['GS',"V","S","P"]:
            continue
        if item.startswith("NEW"):
            continue
        cleaned.append(item)
    return cleaned

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    item = MenuItem(category=title, name="", price=0.0, description="")
    cleaned_items = clean_scraped_text(scraped_text)
    item.price = clean_price(cleaned_items[1])
    item.name = cleaned_items[0]
    if len(cleaned_items) > 2:
        item.description = cleaned_items[2]
    else:
        item.description = "No description available."
    return item



if __name__=='__main__':
    pass
