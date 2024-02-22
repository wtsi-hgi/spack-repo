# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChem16s(RPackage):
	"""Chemical Metrics of Community Reference Proteomes

	Combines taxonomic classifications of high-throughput 16S rRNA
  gene sequences with reference proteomes of archaeal and bacterial taxa to
  generate amino acid compositions of community reference proteomes. Calculates
  chemical metrics including carbon oxidation state ('Zc'), stoichiometric
  oxidation and hydration state ('nO2' and 'nH2O'), H/C, N/C, O/C, and S/C
  ratios, grand average of hydropathicity ('GRAVY'), isoelectric point ('pI'),
  protein length, and average molecular weight of amino acid residues. Uses
  precomputed reference proteomes for archaea and bacteria derived from the
  Genome Taxonomy Database ('GTDB'). Also includes reference proteomes derived
  from the NCBI Reference Sequence ('RefSeq') database and manual mapping from
  the 'RDP Classifier' training set to 'RefSeq' taxonomy as described by Dick and
  Tan (2023) <doi:10.1007/s00248-022-01988-9>. Processes taxonomic
  classifications in 'RDP Classifier' format or OTU tables in 'phyloseq-class'
  objects from the Bioconductor package 'phyloseq'.
	"""
	
	homepage = "https://github.com/jedick/chem16S"
	cran = "chem16S" 

	version("1.0.0", md5="ee800afb0771b544773dca2bc32eea90")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
