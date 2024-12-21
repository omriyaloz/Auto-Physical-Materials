import sys
import json
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QFileDialog,
    QHeaderView,
    QAbstractItemView
)


class DictionaryEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dictionary Editor")
        self.mapping_dict = {}
        self.initUI()

    def initUI(self):
        # Main layout
        mainLayout = QVBoxLayout()

        # Table widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Key", "Values"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.cellChanged.connect(self.updateDictionary)
        mainLayout.addWidget(self.tableWidget)
        
        # Button layout
        buttonLayout = QHBoxLayout()
        
        addRowButton = QPushButton("Add Row")
        addRowButton.clicked.connect(self.addRow)
        buttonLayout.addWidget(addRowButton)

        removeRowButton = QPushButton("Remove Row")
        removeRowButton.clicked.connect(self.removeRow)
        buttonLayout.addWidget(removeRowButton)

        displayDictButton = QPushButton("Display Dictionary")
        displayDictButton.clicked.connect(self.displayDictionary)
        buttonLayout.addWidget(displayDictButton)

        saveButton = QPushButton("Save to JSON")
        saveButton.clicked.connect(self.saveToJson)
        buttonLayout.addWidget(saveButton)

        loadButton = QPushButton("Load from JSON")
        loadButton.clicked.connect(self.loadFromJson)
        buttonLayout.addWidget(loadButton)

        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

    def addRow(self):
        currentRowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(currentRowCount)

        # Make the new row editable
        for col in range(self.tableWidget.columnCount()):
            item = QTableWidgetItem()
            self.tableWidget.setItem(currentRowCount, col, item)
            
    def removeRow(self):
        selected_rows = [index.row() for index in self.tableWidget.selectionModel().selectedRows()]
        if not selected_rows:
            QMessageBox.warning(self, "No Selection", "Please select a row to remove.")
            return

        # Remove rows in reverse order to avoid index issues
        for row in reversed(selected_rows):
            self.tableWidget.removeRow(row)
        self.updateDictionary()

    def updateDictionary(self):
        new_mapping_dict = {}  # Create a new dictionary to avoid modifying the original while iterating
        for row in range(self.tableWidget.rowCount()):
            key_item = self.tableWidget.item(row, 0)
            value_item = self.tableWidget.item(row, 1)

            if key_item and value_item:
                key = key_item.text().strip()
                values_str = value_item.text().strip()

                if key and values_str:
                    values = [v.strip() for v in values_str.split(',')]
                    if key in new_mapping_dict:
                        # Add new values to existing key, avoiding duplicates
                        new_values = [v for v in values if v not in new_mapping_dict[key]]
                        new_mapping_dict[key].extend(new_values)
                    else:
                        new_mapping_dict[key] = values

        self.mapping_dict = new_mapping_dict  # Replace the old dictionary with the new one

    def displayDictionary(self):
        output = ""
        for key, values in self.mapping_dict.items():
            output += f"{key}: {values}\n"

        if output:
            QMessageBox.information(self, "Current Dictionary", output)
        else:
            QMessageBox.information(self, "Empty Dictionary", "The dictionary is empty.")

    def saveToJson(self):
        if not self.mapping_dict:
            QMessageBox.warning(self, "Empty Dictionary", "The dictionary is empty. Nothing to save.")
            return

        filename, _ = QFileDialog.getSaveFileName(self, "Save Dictionary to JSON", "material_mapping", "JSON Files (*.json)")
        if filename:
            try:
                with open(filename, 'w') as f:
                    json.dump(self.mapping_dict, f, indent=4)
                
            except Exception as e:
                QMessageBox.critical(self, "Error Saving File", f"An error occurred: {e}")

    def loadFromJson(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Dictionary from JSON", "", "JSON Files (*.json)")
        if filename:
            try:
                with open(filename, 'r') as f:
                    loaded_dict = json.load(f)  # Load into a temporary dictionary
                self.mapping_dict = loaded_dict  # Replace the old dictionary with the loaded one
                self.populateTable()
                
            except json.JSONDecodeError:
                QMessageBox.critical(self, "Error Loading File", "Invalid JSON format.")
            except Exception as e:
                QMessageBox.critical(self, "Error Loading File", f"An error occurred: {e}")

    def populateTable(self):
        self.tableWidget.setRowCount(0)  # Clear existing rows
        for row_num, (key, values) in enumerate(self.mapping_dict.items()):
            self.tableWidget.insertRow(row_num)
            key_item = QTableWidgetItem(key)
            value_item = QTableWidgetItem(", ".join(values))
            self.tableWidget.setItem(row_num, 0, key_item)
            self.tableWidget.setItem(row_num, 1, value_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = DictionaryEditor()
    editor.show()
    sys.exit(app.exec_())