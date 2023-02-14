import logic


def handle_response(message) -> str:
    p_message: str = message.lower()
    if p_message == "/help":
        return f"**Random episode generator commands:**\n`Family Guy: /theguy`\n`American Dad: /thedad`\n`South Park: /thepark`\n`I Think You Should Leave: /leave`\n`It's Always Sunny in Phillidelphia: /sunny`\n`Trailer Park Boys: /theboys`\n`If you're feeling lucky: /lucky`"
    if p_message == "/theguy":
        result: list = logic.Season_Episode(logic.theGuy)
        return f"**Family Guy S{result[0]} E{result[1]}**"
    if p_message == "/thedad":
        result: list = logic.Season_Episode(logic.theDad)
        return f"**American Dad S{result[0]} E{result[1]}**"
    if p_message == "/thepark":
        result: list = logic.Season_Episode(logic.thePark)
        return f"**South Park S{result[0]} E{result[1]}**"
    if p_message == "/leave":
        result: list = logic.Season_Episode(logic.leave)
        return f"**I Think You Should Leave S{result[0]} E{result[1]}**"
    if p_message == "/sunny":
        result: list = logic.Season_Episode(logic.sunny)
        return f"**It's Aways Sunny in Phillidelphia S{result[0]} E{result[1]}**"
    if p_message == "/theboys":
        result: list = logic.Season_Episode(logic.theBoys)
        return f"**Trailer Park Boys S{result[0]} E{result[1]}**"
    # if p_message == "/NEWSHOW":
        # result: list = logic.Season_Episode(logic.NEWSHOW)
        # return f"**NEWSHOW S{result[0]} E{result[1]}**"

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
        if show == logic.leave:
            result: list = logic.Season_Episode(logic.leave)
            return f"**I Think You Should Leave S{result[0]} E{result[1]}**"
        if show == logic.sunny:
            result: list = logic.Season_Episode(logic.sunny)
            return f"**It's Aways Sunny in Phillidelphia S{result[0]} E{result[1]}**"   
        if show == logic.theBoys:
            result: list = logic.Season_Episode(logic.theBoys)
            return f"**Trailer Park Boys S{result[0]} E{result[1]}**"        
        # if show == logic.NEWSHOW:
        #     result: list = logic.Season_Episode(logic.NEWSHOW)
        #     return f"**NEWSHOW S{result[0]} E{result[1]}**"