def comment_func():
    add_comment = input("Vill du lägga till en kommentar angående den här bryggningen, exempelvis förbättrningsförslag? "
                        "Ange J/N ")
    if add_comment.lower() == "j":
        comment = input("Ange din kommentar här: ")
        return comment
    else:
        comment = "Du har inte sparat någon kommentar."
        return comment


def main():
    comment = comment_func()
    print(comment)


if __name__ == "__main__":
    main()
