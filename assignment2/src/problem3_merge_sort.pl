# ./src/problem3_merge_sort.pl

mergeSort([], []) :- !.
mergeSort([X], [X]) :- !.
mergeSort(List, Sorted) :-
    split2ways(List, Left, Right),
    mergeSort(Left, SortedLeft),
    mergeSort(Right, SortedRight),
    merge(SortedLeft, SortedRight, Sorted).

merge([], L, L).
merge(L, [], L).
merge([F0|R0], [F1|R1], [F0|L]) :-
    F0 < F1,
    merge(R0, [F1|R1], L).
merge([F0|R0], [F1|R1], [F1|L]) :-
    F0 >= F1,
    merge([F0|R0], R1, L).

split2ways(Original, R1, R2) :-
    insertIn1(Original, [], [], R1, R2).

insertIn1([], R1, R2, R1, R2).
insertIn1([H|T], R1, R2, FinalR1, FinalR2) :-
    insertIn2(T, [H|R1], R2, FinalR1, FinalR2).

insertIn2([], R1, R2, R1, R2).
insertIn2([H|T], R1, R2, FinalR1, FinalR2) :-
    insertIn1(T, R1, [H|R2], FinalR1, FinalR2).
