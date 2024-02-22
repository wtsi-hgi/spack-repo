# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvnj(RPackage):
	"""Whole Genome Phylogenies Using Sequence Environments

	Contains utilities for the analysis of protein sequences in a phylogenetic context. 
    Allows   the generation of phylogenetic trees base on protein sequences in an alignment-independent way. 
    Two different methods have been implemented. One approach is based on the frequency analysis of n-grams, 
    previously described in Stuart et al. (2002) <doi:10.1093/bioinformatics/18.1.100>. The other approach is based on the species-specific neighborhood preference around amino acids. Features include the conversion of a protein set into a vector 
    reflecting these neighborhood preferences, pairwise distances (dissimilarity) between these vectors, 
    and the generation of trees based on these distance matrices.
	"""
	
	cran = "EnvNJ" 

	version("0.1.3", md5="47a1a6514058773965e3d50c9db584f1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-bio3d", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
