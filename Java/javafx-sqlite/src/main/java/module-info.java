module com.test.javafxsqlite {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.almasb.fxgl.all;
    requires java.desktop;
    requires java.sql;

    opens com.test.javafxsqlite to javafx.fxml;
    exports com.test.javafxsqlite;
}