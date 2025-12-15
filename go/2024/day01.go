package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// Define the input file path
	inputFile := "../../input/2024/day01.txt"

	// Read the input file and parse the lists
	left, right, err := readInputFile(inputFile)
	if err != nil {
		fmt.Printf("Error reading input file: %v\n", err)
		return
	}

	// Solve Part One: Total Distance
	totalDistance := calculateTotalDistance(left, right)
	fmt.Printf("Part One - Total Distance: %d\n", totalDistance)

	// Solve Part Two: Similarity Score
	similarityScore := calculateSimilarityScore(left, right)
	fmt.Printf("Part Two - Similarity Score: %d\n", similarityScore)
}

// Part One: Calculate the total distance
func calculateTotalDistance(left, right []int) int {
	// Sort both lists
	sort.Ints(left)
	sort.Ints(right)

	// Calculate the total distance
	totalDistance := 0
	for i := range left {
		distance := abs(left[i] - right[i])
		totalDistance += distance
	}
	return totalDistance
}

// Part Two: Calculate the similarity score
func calculateSimilarityScore(left, right []int) int {
	// Create a map to count occurrences in the right list
	rightCounts := make(map[int]int)
	for _, num := range right {
		rightCounts[num]++
	}

	// Calculate the similarity score
	similarityScore := 0
	for _, num := range left {
		count := rightCounts[num]
		similarityScore += num * count
	}
	return similarityScore
}

// Helper function to calculate absolute value
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Read input file and parse left and right lists
func readInputFile(filepath string) ([]int, []int, error) {
	file, err := os.Open(filepath)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	var left, right []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		// Split the line into two parts
		parts := strings.Fields(line)
		if len(parts) != 2 {
			return nil, nil, fmt.Errorf("invalid line format: %s", line)
		}

		// Convert strings to integers and append to lists
		leftVal, err := strconv.Atoi(parts[0])
		if err != nil {
			return nil, nil, fmt.Errorf("invalid integer: %s", parts[0])
		}
		rightVal, err := strconv.Atoi(parts[1])
		if err != nil {
			return nil, nil, fmt.Errorf("invalid integer: %s", parts[1])
		}

		left = append(left, leftVal)
		right = append(right, rightVal)
	}

	// Check for scanner errors
	if err := scanner.Err(); err != nil {
		return nil, nil, err
	}

	return left, right, nil
}
