#pragma once    

typedef enum{
    niski, sredni, wysoki
} Wzrost;

typedef struct 
{
    char imie[30];
    char nazwisko[30];
    Wzrost wzrost;
} Person;
