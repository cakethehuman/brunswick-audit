package main

import (
	"fmt"
	"os"
	"strings"
)

func main2() {
	// file paths

	filePath := "data_inputs/data_input.txt"
	newFilePath := "special spikey/data.csv"

	content, err := os.ReadFile(filePath)
	if err != nil {
		fmt.Printf("Error reading file: %s\n", err)
		os.Exit(1)
	}

	text := string(content)

	newText := strings.ReplaceAll(text, " ", ",")

	features := "name,kills,death,ast\n"
	newText = features + newText

	err = os.WriteFile(newFilePath, []byte(newText), 0644)
	if err != nil {
		fmt.Printf("Error writing to file: %s\n", err)
		os.Exit(1)
	}

	fmt.Println("File modified successfully")
}
