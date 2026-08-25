func groupAnagrams(strs []string) [][]string {
	if len(strs) < 1 {
		return [][]string{{}}
	}

	res := make(map[[26]int][]string)

	for _, word := range strs {
		var start [26]int
		for _, r := range word {
			start[r-'a']++
		}
		res[start] = append(res[start], word)
	}

	var result [][]string
	for _, group := range res {
		result = append(result, group)
	}
	return result
}
