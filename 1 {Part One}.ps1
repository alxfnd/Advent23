$puzzleInput = Get-Content ".\PowerShell\AoC\1.txt"

$numbersList = @('1','2','3','4','5','6','7','8','9','0')

$puzzlesAnswers = @()
foreach ($inputLine in $puzzleInput) {
    $validValues = @()
    $stringIterator = 0
    while ($stringIterator -ne $inputLine.Length) {
        $currentValue = $inputLine[$stringIterator]
        if ($numbersList.Contains([string]$currentValue)) { $validValues += $currentValue }
        $stringIterator += 1
    }
    $puzzlesAnswers += ($validValues[0] + $validValues[-1])
}

$answerOne = 0
$validValuesCounter = 0
while ($validValuesCounter -ne $puzzlesAnswers.Count) {
    $answerOne += $puzzlesAnswers.Get($validValuesCounter)
    $validValuesCounter += 1
}
"That answer to question one is: " + $answerOne
