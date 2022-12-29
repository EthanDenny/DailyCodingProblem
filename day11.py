def f(s, queries):
    return {q for q in queries if q.startswith(s)}


if __name__ == "__main__":
    assert f("de", {"dog", "deer", "deal"}) == {"deer", "deal"}
