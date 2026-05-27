import simple_hello


def main():
    simple_hello.print_hello()
    a = simple_hello.Hello("park")
    print(a.name)
    print(a.greet())


if __name__ == "__main__":
    main()