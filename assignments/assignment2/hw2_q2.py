from enum import Enum
from collections import namedtuple

from itertools import chain, zip_longest


Type = Enum("Type", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks.
    Taken directly from https://docs.python.org/3/library/itertools.html#itertools-recipes.

    Example
    -------
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def treat_cure(left, right):
    if right is None:
        return (left,)
    if right.category is Type.CURE:
        return left, right
    elif right.category is Type.SICK:
        return left, Agent(right.name, Type.HEALTHY)
    elif right.category is Type.DYING:
        return left, Agent(right.name, Type.SICK)


def treat_sick(left, right):
    if right is None:
        return (left,)
    if right.category is Type.CURE:
        return Agent(left.name, Type.HEALTHY), right
    elif right.category is Type.SICK:
        return Agent(left.name, Type.DYING), Agent(right.name, Type.DYING)
    elif right.category is Type.DYING:
        return Agent(left.name, Type.DYING), Agent(right.name, Type.DEAD)


def treat_dying(left, right):
    if right is None:
        return (left,)
    if right.category is Type.CURE:
        return Agent(left.name, Type.SICK), right
    elif right.category is Type.SICK:
        return Agent(left.name, Type.DEAD), Agent(right.name, Type.DYING)
    elif right.category is Type.DYING:
        return Agent(left.name, Type.DEAD), Agent(right.name, Type.DEAD)


type_to_function_switch = {
    Type.CURE: treat_cure,
    Type.SICK: treat_sick,
    Type.DYING: treat_dying,
}


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Type.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    # First we filter our original agents listing - DEAD and HEALTHY ones
    # are immediately thrown to the "updated_listing" list which we'll
    # return, and the rest will be processed.
    relevant_agents = []
    updated_listing = []
    for agent in agent_listing:
        if (agent.category is Type.DEAD) or (agent.category is Type.HEALTHY):
            updated_listing.append((agent,))
        else:
            relevant_agents.append(agent)

    for inp in grouper(relevant_agents, 2):
        updated_listing.append(type_to_function_switch[inp[0].category](inp[0], inp[1]))
    updated_listing = chain.from_iterable(updated_listing)
    return list(updated_listing)
