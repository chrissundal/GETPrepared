package com.test.javafxsqlite;

public class Person {
    private Integer id;
    private String name;
    private String userName;

    public Person(Integer id, String name, String userName) {
        this.id = id;
        this.name = name;
        this.userName = userName;
    }

    public String GetName() {
        return name;
    }

    @Override
    public String toString() {
        return "Bruker: " + userName;
    }


    public Integer getId() {
        return id;
    }

    public String GetUserName() {
        return userName;
    }
}
