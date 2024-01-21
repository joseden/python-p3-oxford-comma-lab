def oxford_comma(items):
    """Returns a string with the Oxford comma (", and") before the last item,
    but only for lists of three or more items."""
    if len(items) == 1:
        return items[0]  # No comma needed for a single item
    elif len(items) == 2:
        return " and ".join(items)  # Join with "and" for a 2-element list
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]  # Add Oxford comma

items = ['apple', 'banana', 'orange', 'grape']
result = oxford_comma(items)
print(result)

