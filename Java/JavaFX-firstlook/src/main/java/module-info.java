module com.example.javafxfirstlook {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;


    opens com.example.javafxfirstlook to javafx.fxml;
    exports com.example.javafxfirstlook;
}