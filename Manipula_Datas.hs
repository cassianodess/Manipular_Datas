-- Cassiano de Souza Santos -- Manipulação de Datas em Haskell

data Data = MinhaData String Int Int Int | DataComemorativa String Int Int Int
    deriving(Show)


nome :: Data -> String
nome (MinhaData x _ _ _) = x
nome (DataComemorativa a _ _ _) = a

dia :: Data -> Int
dia (MinhaData _ y _ _) = y
dia (DataComemorativa _ b _ _) = b

mes :: Data -> Int
mes (MinhaData _ _ z _) = z
mes (DataComemorativa _ _ c _) = c

ano :: Data -> Int
ano (MinhaData _ _ _ w) = w
ano (DataComemorativa _ _ _ d) = d

split :: Eq a => a -> [a] -> [[a]]
split d [] = []
split d s = x : split d (drop 1 y) where (x,y) = span (/= d) s

toString :: Data -> [Char]
toString (MinhaData _ x y z) = show x ++ show y ++ show z
toString (DataComemorativa _ a b c) = show a ++ show b ++ show c


compara :: Data -> Data -> Int
compara (MinhaData _ x y z) (MinhaData _ a b c) 
    | (x == a) && (y == b) && (z == c) = 0
    | (z == c) && (y == b) && (x > a) = 1
    | (z == c) && (y == b) && (x < a) = -1
    | (z == c) && (y > b) = 1
    | (z == c) && (y < b) = -1
    | (z > c) = 1
    | otherwise = -1
compara (DataComemorativa _ x y z) (DataComemorativa _ a b c) 
    | (x == a) && (y == b) && (z == c) = 0
    | (z == c) && (y == b) && (x > a) = 1
    | (z == c) && (y == b) && (x < a) = -1
    | (z == c) && (y > b) = 1
    | (z == c) && (y < b) = -1
    | (z > c) = 1
    | otherwise = -1
compara (MinhaData _ x y z) (DataComemorativa _ a b c) 
    | (x == a) && (y == b) && (z == c) = 0
    | (z == c) && (y == b) && (x > a) = 1
    | (z == c) && (y == b) && (x < a) = -1
    | (z == c) && (y > b) = 1
    | (z == c) && (y < b) = -1
    | (z > c) = 1
    | otherwise = -1
compara (DataComemorativa _ x y z) (MinhaData _ a b c) 
    | (x == a) && (y == b) && (z == c) = 0
    | (z == c) && (y == b) && (x > a) = 1
    | (z == c) && (y == b) && (x < a) = -1
    | (z == c) && (y > b) = 1
    | (z == c) && (y < b) = -1
    | (z > c) = 1
    | otherwise = -1

adiciona :: Data -> [Data]
adiciona (DataComemorativa a b c d) = []++[(DataComemorativa a b c d)]

-- DatasComemorativas :: Data -> [Data]
-- DatasComemorativas (DataComemorativa a b c d) = []++[(DataComemorativa a b c d)]


-- remove :: String -> [Data] -> [Data]
-- remove _ [] = []
-- remove x [(DataComemorativa a b c d )]  
--     | (elem x [(DataComemorativa a b c d )] == True) = [filter (/= x) [(DataComemorativa a b c d )]]
--     | otherwise [(DataComemorativa a b c d )]

horas_nao_trabalhadas :: [Data] -> Int
horas_nao_trabalhadas [] = 0
horas_nao_trabalhadas (x:xs) = 8 + horas_nao_trabalhadas xs

---------------------------------------- main ------------------------------------------

atual :: Data
atual = MinhaData "atual" 11 12 2020

natal :: Data
natal = DataComemorativa "natal" 25 12 2020

x = compara atual natal
z = horas_nao_trabalhadas y

y = adiciona natal


