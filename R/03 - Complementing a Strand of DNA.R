reverse_complement <- function(dna_string) {
  complement <- chartr('GCAT', 'CGTA', dna_string)
  complement_vec <-  strsplit(complement, split='')[[1]]
  reverse_complement <- paste0(rev(complement_vec), collapse='')
  print(reverse_complement)
}

reverse_complement('GCAT')
