# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRainbowr(RPackage):
	"""Genome-Wide Association Study with SNP-Set Methods

	By using 'RAINBOWR' (Reliable Association INference By Optimizing Weights with R), users can test multiple SNPs (Single Nucleotide Polymorphisms) simultaneously by kernel-based (SNP-set) methods. This package can also be applied to haplotype-based GWAS (Genome-Wide Association Study). Users can test not only additive effects but also dominance and epistatic effects. In detail, please check our paper on PLOS Computational Biology: Kosuke Hamazaki and Hiroyoshi Iwata (2020) <doi:10.1371/journal.pcbi.1007663>.
	"""
	
	cran = "RAINBOWR" 

	version("0.1.35", md5="c5da8feb805af0b3ed13216abfaed302")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
	depends_on("r-rrblup", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-gaston", type=("build", "run"))
	depends_on("r-mm4lmm", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
