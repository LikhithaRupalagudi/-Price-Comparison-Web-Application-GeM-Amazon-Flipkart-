def get_gem_price(product_name):
    product_name = product_name.lower()

    gem_data = {
        # IT Products
        "desktop computer": ("₹32,000", "https://gem.gov.in/search?q=desktop+computer"),
        "laptop notebook": ("₹42,000", "https://gem.gov.in/search?q=laptop+notebook"),
        "computer printer": ("₹9,500", "https://gem.gov.in/search?q=computer+printer"),
        "tablet computer": ("₹15,000", "https://gem.gov.in/search?q=tablet+computer"),

        "electronics" : ("1599", "https://mkp.gem.gov.in/search?q=it+products"),
        "television": ("5000", "https://mkp.gem.gov.in/domestic-appliances-and-supplies-and-consumer-electronic-products-consumer-electronics-audio-and-visual-equipmentold-television-tv-v2-/search"),
        "tv": ("₹25,000", "https://gem.gov.in/search?q=tv"),
        "domestic refrigerator": ("₹18,500", "https://gem.gov.in/search?q=domestic+refrigerator"),

        
        "furniture": ("1499", "https://mkp.gem.gov.in/search?q=furniture"),
        "class room desking": ("₹4,000", "https://gem.gov.in/search?q=class+room+desking"),
        "executive table": ("₹6,500", "https://gem.gov.in/search?q=executive+table"),
        "revolving chair": ("₹3,800", "https://gem.gov.in/search?q=revolving+chair"),
        "movable file storage system": ("₹5,200", "https://gem.gov.in/search?q=movable+file+storage+system"),
    }

    for key in gem_data:
        if key in product_name:
            return gem_data[key]

    # If product not found in the predefined list
    return "Price Not Found", "https://gem.gov.in/search?q=" + product_name.replace(" ", "+")
