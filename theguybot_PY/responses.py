import logic


def handle_response(message) -> str:
    p_message: str = message.lower()
    if p_message == "/theguy":
        result: list = logic.Season_Episode(logic.theGuy)
        return f"**Family Guy S{result[0]} E{result[1]}**"
    if p_message == "/thedad":
        result: list = logic.Season_Episode(logic.theDad)
        return f"**American Dad S{result[0]} E{result[1]}**"
    if p_message == "/thepark":
        result: list = logic.Season_Episode(logic.thePark)
        return f"**South Park S{result[0]} E{result[1]}**"
    if p_message == "/lucky":
        show = logic.Show_Picker()
        if show == logic.theGuy:
            result: list = logic.Season_Episode(logic.theGuy)
            return f"**Family Guy S{result[0]} E{result[1]}**"
        if show == logic.theDad:
            result: list = logic.Season_Episode(logic.theDad)
            return f"**American Dad S{result[0]} E{result[1]}**"
        if show == logic.thePark:
            result: list = logic.Season_Episode(logic.thePark)
            return f"**South Park S{result[0]} E{result[1]}**"
    if p_message == "/help":
        return f"**Commands:**\n`For Family Guy: /theguy`\n`For American Dad: /thedad`\n`For South Park: /thepark`\n`If you're feeling lucky: /lucky`"