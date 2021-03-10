transcribe_dna <- function(dna_string) {
  rna_string <- gsub('T', 'U', dna_string)
  print(rna_string)
}

transcribe_dna('ACGT')