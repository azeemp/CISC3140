(define (mergelists lst1 lst2)
  (cond ((null? lst1) lst2)
        ((null? lst2) lst1)
        ((>= (car lst1) (car lst2))
         (cons (car lst2) (mergelists lst1 (cdr lst2))))
        (else
         (cons (car lst1) (mergelists (cdr lst1) lst2)))))

;try (mergelists '(1 3 4) '(2 4 5))
         
