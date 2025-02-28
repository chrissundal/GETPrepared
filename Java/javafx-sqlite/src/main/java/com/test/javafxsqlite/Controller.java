package com.test.javafxsqlite;

import java.sql.*;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class Controller {
    private Connection conn;
    private ObservableList<Person> people = FXCollections.observableArrayList();
    @FXML
    private ListView<Person> listView = new ListView<>();

    @FXML
    private TextField editName;

    @FXML
    private TextField editUserName;

    @FXML
    private TextField nameInput;

    @FXML
    private TextField usernameInput;

    @FXML
    private VBox vboxAdd;

    @FXML
    private VBox vboxFront;

    @FXML
    private VBox vboxEdit;

    @FXML
    void cancelEdit(ActionEvent event) {
        vboxAdd.setVisible(false);
        vboxFront.setVisible(true);
        vboxEdit.setVisible(false);
        editName.setText("");
        editUserName.setText("");
    }

    @FXML
    void addNew(ActionEvent event) {
        String name = nameInput.getText();
        String username = usernameInput.getText();
        insertData(name, username);
        fetchData();
        vboxAdd.setVisible(false);
        vboxFront.setVisible(true);
    }
    @FXML
    void cancel(ActionEvent event) {
        vboxAdd.setVisible(false);
        vboxFront.setVisible(true);
    }

    @FXML
    void refreshList(ActionEvent event) {
        setListView();
    }
    @FXML
    void remove(ActionEvent event) {
        Person selected = listView.getSelectionModel().getSelectedItem();
        removeData(selected.getId());
        fetchData();
    }
    @FXML
    void add(ActionEvent event) {
        vboxAdd.setVisible(true);
        vboxFront.setVisible(false);
    }

    @FXML
    void editUser(ActionEvent event) {
        Person selected = listView.getSelectionModel().getSelectedItem();
        vboxAdd.setVisible(false);
        vboxFront.setVisible(false);
        vboxEdit.setVisible(true);
        editName.setText(selected.GetName());
        editUserName.setText(selected.GetUserName());
    }
    @FXML
    void updateUser(ActionEvent event) {
        Person selected = listView.getSelectionModel().getSelectedItem();
        String name = selected.GetName();
        String username = selected.GetUserName();
        boolean isUpdated = false;
        if(!name.equals(editName.getText())){
            name = editName.getText();
            isUpdated = true;
        }
        if(!username.equals(editUserName.getText())) {
            username = editUserName.getText();
            isUpdated = true;
        }
        if(isUpdated) {
            updateData(selected.getId(), name, username);
            editName.setText("");
            editUserName.setText("");
            vboxAdd.setVisible(false);
            vboxFront.setVisible(true);
            vboxEdit.setVisible(false);
            fetchData();
        } else {
            System.out.println("Ikke oppdatert");
        }

    }

    public void initialize() {
        printList();
        if(ConnectDb()){
            fetchData();
            listView.setItems(people);
        } else {
            System.out.println("Database connection failed");
        }
    }
    void printList() {
        for (Person pep : people) {
            System.out.println(pep.GetName());
        }
    }
    void setListView(){
        fetchData();
        listView.setItems(people);
    }
    private Boolean ConnectDb() {
        try {
            if (conn == null || conn.isClosed()) {
                conn = DriverManager.getConnection("jdbc:sqlite:firstDB.db");
                System.out.println("Database connected");
                return true;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }


    private void fetchData() {
        try {
            String query = "SELECT * FROM personSql";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            people.clear();
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String userName = rs.getString("username");
                Person person = new Person(id, name, userName);
                people.add(person);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void insertData(String name, String username) {
        String query = "INSERT INTO personSql (name, username) VALUES (?, ?)";
        try (PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.setString(1, name);
            pstmt.setString(2, username);
            pstmt.executeUpdate();
            System.out.println("Data inserted successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    private void removeData(Integer id) {
        String query = "DELETE FROM personSql WHERE id = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
            System.out.println("Data deleted successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    private void updateData(Integer id, String name, String username) {
        String query = "UPDATE personSql SET name = ?, username = ? WHERE id = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.setString(1, name);
            pstmt.setString(2, username);
            pstmt.setInt(3, id);
            pstmt.executeUpdate();
            System.out.println("Data updated successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void closeConnection() {
        try {
            if (conn != null && !conn.isClosed()) {
                conn.close();
                System.out.println("Database connection closed");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

}