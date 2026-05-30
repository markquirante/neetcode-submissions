func groupAnagrams(strs []string) [][]string {
    
    // I need to generate a new list for each group

    // each element in the new sublists are all the same length

    // group all strings that are the same length

    groups := make(map[int][]string)

    // groups words with the same length
    for _, str := range strs {
        length := len(str)
        groups[length] = append(groups[length], str)
    }

    groupedWordLength := [][]string{}

    // appends all sublist in result
    for _, sublist := range groups {
        groupedWordLength = append(groupedWordLength, sublist)
    }

    // create a helper function to validate anagram
    isAnagram := func(s string, t string) bool {
        if len(s) != len(t) {
            return false
        }

        counts := make(map[rune]int)

        // Count characters in the first string
        for _, r := range s {
            counts[r]++
        }

        // Subtract counts using the second string
        for _, r := range t {
            counts[r]--
            if counts[r] < 0 {
                return false
            }
        }

        return true
    }

    // group anagrams, if not make new list

    sortedAnagrams := [][]string{}

    for _, sublist := range groupedWordLength {
        var anagramGroups [][]string

        for _, str := range sublist {
            foundGroup := false

            for i, group := range anagramGroups {
                if isAnagram(str, group[0]) {
                    anagramGroups[i] = append(anagramGroups[i], str)
                    foundGroup = true
                    break
                }
            }

            if !foundGroup {
                anagramGroups = append(anagramGroups, []string{str})
            }
        }

        sortedAnagrams = append(sortedAnagrams, anagramGroups...)
    }
    
    return sortedAnagrams
}
