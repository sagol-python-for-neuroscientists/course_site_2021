""" Tests for question 2 - Spreading Virus """

from hw2_q2 import meetup, Type, Agent


data0 = (
    Agent("Adam", Type.SICK),
    Agent("Cure0", Type.CURE),
    Agent("Cure1", Type.CURE),
    Agent("Bob", Type.HEALTHY),
    Agent("Alice", Type.DEAD),
    Agent("Charlie", Type.DYING),
    Agent("Vaccine", Type.SICK),
    Agent("Darlene", Type.DYING),
    Agent("Emma", Type.SICK),
    Agent("Cure2", Type.CURE),
)

data1 = (Agent("Buddy", Type.CURE), Agent("Holly", Type.DEAD))

data2 = (
    Agent("Zelda0", Type.SICK),
    Agent("Zelda1", Type.SICK),
    Agent("Zelda2", Type.SICK),
    Agent("Zelda3", Type.SICK),
    Agent("Zelda4", Type.DEAD),
    Agent("Zelda5", Type.HEALTHY),
)

data3 = (
    Agent("Mark", Type.SICK),
    Agent("Mork", Type.HEALTHY),
    Agent("Harry", Type.DYING),
    Agent("Cure", Type.CURE),
    Agent("Lora", Type.SICK),
    Agent("Monica", Type.SICK),
)

data4 = (
    Agent("Robert", Type.SICK),
)

data5 = ()


def test_data0():
    code_result = set(meetup(data0))
    true_result = {
        Agent(name="Adam", category=Type.HEALTHY),
        Agent(name="Alice", category=Type.DEAD),
        Agent(name="Bob", category=Type.HEALTHY),
        Agent(name="Charlie", category=Type.SICK),
        Agent(name="Cure0", category=Type.CURE),
        Agent(name="Cure1", category=Type.CURE),
        Agent(name="Cure2", category=Type.CURE),
        Agent(name="Darlene", category=Type.DEAD),
        Agent(name="Emma", category=Type.HEALTHY),
        Agent(name="Vaccine", category=Type.DYING),
    }
    assert code_result == true_result


def test_data1():
    code_result = set(meetup(data1))
    true_result = set(data1)
    assert code_result == true_result


def test_data2():
    code_result = set(meetup(data2))
    true_result = set(
        [
            Agent("Zelda0", Type.DYING),
            Agent("Zelda1", Type.DYING),
            Agent("Zelda2", Type.DYING),
            Agent("Zelda3", Type.DYING),
            Agent("Zelda4", Type.DEAD),
            Agent("Zelda5", Type.HEALTHY),
        ]
    )
    assert code_result == true_result


def test_data3():
    code_result = set(meetup(data3))
    true_result = set(
        [
            Agent("Mark", Type.DYING),
            Agent("Mork", Type.HEALTHY),
            Agent("Harry", Type.DEAD),
            Agent("Cure", Type.CURE),
            Agent("Lora", Type.HEALTHY),
            Agent("Monica", Type.SICK),
        ]
    )
    assert code_result == true_result


def test_data4():
    code_result = set(meetup(data4))
    true_result = {Agent("Robert", Type.SICK)}
    assert code_result == true_result


def test_data5():
    code_result = meetup(data5)
    true_result = []
    assert code_result == true_result


def test_data6():
    code_result = meetup(data5)
    assert isinstance(code_result, list)


if __name__ == "__main__":
    methods = [f"test_data{num}" for num in range(7)]
    errors = []

    for method in methods:
        try:
            eval(method)()
        except Exception as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")
    if len(errors) > 0:
        print(errors)
    else:
        print("Tests pass successfully.")
