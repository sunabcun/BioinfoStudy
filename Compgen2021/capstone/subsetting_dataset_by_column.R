BROAD_training6 <- readRDS("D:/VMshared/compgen2021/BROAD/training6.Rds")
SANGER_training6 <- readRDS("D:/VMshared/compgen2021/SANGER/training6.Rds")
CCLE_training6 <- readRDS("D:/VMshared/compgen2021/CCLE/training6.Rds")
PDX_training6 <- readRDS("D:/VMshared/compgen2021/PDX/training6.Rds")

t <- intersect(names(BROAD_training6), names(CCLE_training6))
t2 <- intersect(names(PDX_training6), names(CCLE_training6))
t3 <- intersect(names(SANGER_training6), names(CCLE_training6))

cols_remove <- t2

BROAD_training6_sub <- BROAD_training6[, (colnames(BROAD_training6) %in% cols_remove)]
SANGER_training6_sub <- SANGER_training6[, (colnames(SANGER_training6) %in% cols_remove)]
CCLE_training6_sub <- CCLE_training6[, (colnames(CCLE_training6) %in% cols_remove)]
PDX_training6_sub <- PDX_training6[, (colnames(PDX_training6) %in% cols_remove)]

t <- intersect(names(BROAD_training6_sub), names(CCLE_training6_sub))
t2 <- intersect(names(PDX_training6_sub), names(CCLE_training6_sub))
t3 <- intersect(names(SANGER_training6_sub), names(CCLE_training6_sub))

cols_remove <- t

BROAD_training6_sub <- BROAD_training6[, (colnames(BROAD_training6) %in% cols_remove)]
SANGER_training6_sub <- SANGER_training6[, (colnames(SANGER_training6) %in% cols_remove)]
CCLE_training6_sub <- CCLE_training6[, (colnames(CCLE_training6) %in% cols_remove)]
PDX_training6_sub <- PDX_training6[, (colnames(PDX_training6) %in% cols_remove)]

t <- intersect(names(BROAD_training6_sub), names(CCLE_training6_sub))
t2 <- intersect(names(PDX_training6_sub), names(CCLE_training6_sub))
t3 <- intersect(names(SANGER_training6_sub), names(CCLE_training6_sub))

cols_remove <- t3

BROAD_training6_sub <- BROAD_training6[, (colnames(BROAD_training6) %in% cols_remove)]
SANGER_training6_sub <- SANGER_training6[, (colnames(SANGER_training6) %in% cols_remove)]
CCLE_training6_sub <- CCLE_training6[, (colnames(CCLE_training6) %in% cols_remove)]
PDX_training6_sub <- PDX_training6[, (colnames(PDX_training6) %in% cols_remove)]

my_func <- function(x,y) {
  for (i in names(x)) {
    if (!(i %in% names(y))) {
      print('Warning: Names are not the same')
      break
    }  
    else if(i==tail(names(y),n=1)) {
      print('Names are identical')
    }
  }
}

my_func(BROAD_training6_sub, SANGER_training6_sub)
my_func(BROAD_training6_sub, CCLE_training6_sub)
my_func(BROAD_training6_sub, PDX_training6_sub)
my_func(CCLE_training6_sub, SANGER_training6_sub)
my_func(PDX_training6_sub, SANGER_training6_sub)
my_func(CCLE_training6_sub, PDX_training6_sub)

saveRDS(BROAD_training6_sub, "D:/VMshared/compgen2021/BROAD/training6.Rds")
saveRDS(SANGER_training6_sub, "D:/VMshared/compgen2021/SANGER/training6.Rds")
saveRDS(CCLE_training6_sub, "D:/VMshared/compgen2021/CCLE/training6.Rds")
saveRDS(PDX_training6_sub, "D:/VMshared/compgen2021/PDX/training6.Rds")

