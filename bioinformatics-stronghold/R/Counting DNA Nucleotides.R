nucleotide_counter <- function (dna_string) {
  library(stringr)
  count <- str_count(string=dna_string, pattern= c("A","C","G","T"))
  print(count)
}

nucleotide_counter("ACGT")
