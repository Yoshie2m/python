import dataclasses


@dataclasses.dataclass(frozen=True)
class FullName:
    familyName: str
    firstName: str


def abc():
    print("abc")


def main():
    full_name = FullName("Yoko", "Taro")
    print(full_name.familyName)


if __name__ == '__main__':
    main()
