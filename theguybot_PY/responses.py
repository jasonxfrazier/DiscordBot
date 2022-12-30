import logic


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == "/theguy":
        result = logic.Season_Episode(logic.theGuy)
        return f"**Family Guy S{result[0]} E{result[1]}**"

    if p_message == "/thedad":
        result = logic.Season_Episode(logic.theDad)
        return f"**American Dad S{result[0]} E{result[1]}**"

    if p_message == "/thepark":
        result = logic.Season_Episode(logic.thePark)
        return f"**South Park S{result[0]} E{result[1]}**"

    if p_message == "/lucky":
        show = logic.Show_Picker()
        if show == logic.theGuy:
            result = logic.Season_Episode(logic.theGuy)
            return f"**Family Guy S{result[0]} E{result[1]}**"
        if show == logic.theDad:
            result = logic.Season_Episode(logic.theDad)
            return f"**American Dad S{result[0]} E{result[1]}**"
        if show == logic.thePark:
            result = logic.Season_Episode(logic.thePark)
            return f"**South Park S{result[0]} E{result[1]}**"

    if p_message == "/help":
        return f"**Commands:**\n`/theguy`\n`/thedad`\n`/thepark`\n`/lucky`"