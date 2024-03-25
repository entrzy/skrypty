Round Robin – prosta metoda, która przekierowuje ruch do serwerów po kolei, równomiernie rozdzielając obciążenie. Kiedy lista serwerów dobiegnie końca, cykl rozpoczyna się od nowa.

Least Connections – metoda ta kieruje ruch do serwera z najmniejszą liczbą aktywnych połączeń. Jest szczególnie efektywna w sytuacjach, gdy czas obsługi zapytania jest zmienny.

Fastest Response – ruch jest kierowany do serwera, który najszybciej odpowiada na zapytania. Metoda ta jest użyteczna w środowiskach, gdzie czas odpowiedzi jest krytyczny.

IP Hash – metoda ta wykorzystuje adres IP źródłowy klienta do wyboru serwera. Zapewnia to, że użytkownik zawsze zostanie połączony z tym samym serwerem, co może być ważne dla zachowania sesji użytkownika.

Dynamic Ratio – metoda ta polega na dynamicznym przydzielaniu ruchu na podstawie wydajności serwerów. Wykorzystuje do tego celu różne wskaźniki, takie jak obciążenie CPU lub ilość pamięci RAM, aby określić, który serwer jest w stanie obsłużyć więcej ruchu.

Priority Group Activation – pozwala na definiowanie priorytetów dla grup serwerów. Ruch jest najpierw kierowany do serwerów o najwyższym priorytecie. Gdy te serwery są przeciążone lub niedostępne, ruch jest przekierowywany do serwerów z niższym priorytetem.

Weighted – w tej metodzie administrator może przypisać wagi do poszczególnych serwerów w puli. Serwery z wyższą wagą będą otrzymywać więcej ruchu w porównaniu do serwerów z niższą wagą.

Source Address Affinity (Session Persistence) – metoda ta zapewnia, że żądania od określonego adresu IP zawsze będą kierowane do tego samego serwera. Jest to przydatne w aplikacjach, które wymagają utrzymania stanu sesji.
