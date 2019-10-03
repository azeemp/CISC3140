(define (ispalindrome? b)
  (let ((chars (string->list b)))
    (equal? chars (reverse chars))))
   
;try (ispalindrome? "racecar")
