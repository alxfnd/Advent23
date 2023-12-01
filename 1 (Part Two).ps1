$puzzleInput = Get-Content ".\PowerShell\AoC\1.txt"

$numbersList = @('1','2','3','4','5','6','7','8','9','0','one','two','three','four','five','six','seven','eight','nine')

$puzzlesAnswers = @()
foreach ($inputLine in $puzzleInput) {
    $validValues= @()
    $stringScanCounter = 0
    $firstMatch = 0
    while ($firstMatch -eq 0) {
        $stringScan = $inputLine.Substring($stringScanCounter)
        foreach ($number in $numbersList) {
            if ($stringScan.StartsWith($number)) {
                $positionOfNumberInList = $numbersList.IndexOf($number)
                if ($positionOfNumberInList -gt 9) {
                    $validValues += $numbersList[($positionOfNumberInList - 10)]
                }else{
                    $validValues += $number
                }
                $firstMatch = 1
            }
        }
        $stringScanCounter += 1
    }
    $stringScanCounter = ($inputLine.Length - 1)
    $secondMatch = 0
    while ($secondMatch -eq 0) {
        $stringScan = $inputLine.Substring($stringScanCounter)
        foreach ($number in $numbersList) {
            if ($stringScan.StartsWith($number)) {
                $positionOfNumberInList = $numbersList.IndexOf($number)
                if ($positionOfNumberInList -gt 9) {
                    $validValues += $numbersList[($positionOfNumberInList - 10)]
                }else{
                    $validValues += $number
                }
                $secondMatch = 1
            }
        }
        $stringScanCounter -= 1
    }
    $puzzlesAnswers += ($validValues[0] + $validValues[-1])
}

$answerTwo = 0
$validValuesCounter = 0
while ($validValuesCounter -ne $puzzlesAnswers.Count) {
    $answerTwo += $puzzlesAnswers.Get($validValuesCounter)
    $validValuesCounter += 1
}
"That answer to question two is: " + $answerTwo
