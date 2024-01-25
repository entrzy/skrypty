
Uzasadnienie Techniczne:

W obliczu rosnących wymagań wydajnościowych naszej aplikacji AML, stwierdzono konieczność rozbudowy infrastruktury serwerowej. Obecna konfiguracja nie jest w stanie sprostać zwiększonemu obciążeniu wynikającemu z podwojenia liczby systemów integrujących się z naszym rozwiązaniem w ciągu ostatnich dwóch lat. Analiza wydajności wykazała, że przeciążenie serwerów prowadzi do znacznego wydłużenia czasu odpowiedzi aplikacji, co bezpośrednio wpływa na efektywność operacji związanych z przeciwdziałaniem praniu pieniędzy.

Konkretnie, zidentyfikowano potrzebę dodania 2x vCPU do każdego z dwóch serwerów obsługujących ruch sieciowy. Obecne serwery działają na granicy swoich możliwości, co skutkuje opóźnieniami i potencjalnymi przestojami. Dodatkowo, serwer IBM WebSphere, który jest rdzeniem przetwarzania danych aplikacji AML, wymaga rozbudowy o 2x vCPU. Podobna potrzeba dotyczy serwera IBM SPSS Modeler Server, który odpowiada za zaawansowaną analizę danych. W obu przypadkach, rozbudowa wiąże się z dodatkowymi kosztami licencyjnymi.

Definition of Done:

Dodanie vCPU do Serwerów Sieciowych: Zakończenie procesu instalacji dodatkowych 2x vCPU na każdym z dwóch serwerów sieciowych, potwierdzone testami wydajności.

Rozbudowa IBM WebSphere: Skuteczne dodanie 2x vCPU do serwera IBM WebSphere, z potwierdzeniem poprawy wydajności przetwarzania.

Upgrade IBM SPSS Modeler Server: Zainstalowanie 2x vCPU na serwerze IBM SPSS Modeler Server, z weryfikacją poprawy wydajności analitycznej.

Testy Wydajnościowe: Przeprowadzenie i dokumentacja testów wydajnościowych po rozbudowie, potwierdzających osiągnięcie założonych celów wydajnościowych.

Monitorowanie Post-Implementacyjne: Ustalenie procesu ciągłego monitorowania wydajności systemu po rozbudowie, z możliwością szybkiej interwencji i optymalizacji.

Opis Korzyści:

Zwiększona Przepustowość: Dodatkowe vCPU pozwolą na obsługę większej liczby równoczesnych zapytań, redukując czas odpowiedzi.

Stabilność Systemu: Rozbudowa zasobów serwerowych zmniejszy ryzyko przeciążeń i awarii, zwiększając niezawodność systemu.

Lepsza Skalowalność: Ulepszona infrastruktura pozwoli na elastyczne dostosowanie do przyszłego wzrostu zapotrzebowania.

Optymalizacja Kosztów Długoterminowych: Inwestycja w rozbudowę serwerów przyczyni się do zwiększenia efektywności operacyjnej, co może obniżyć koszty eksploatacyjne w dłuższej perspektywie.

Zgodność z Regulacjami: Szybsze przetwarzanie i analiza danych ułatwią przestrzeganie przepisów AML, podnosząc poziom bezpieczeństwa i zgodności.
