# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaresim(RPackage):
	"""Simulation of Rare Variant Genetic Data

	Haplotype simulations of rare variant genetic data that emulates real data can be performed with RAREsim. RAREsim uses the expected number of variants in MAC bins - either as provided by default parameters or estimated from target data - and an abundance of rare variants as simulated HAPGEN2 to probabilistically prune variants. RAREsim produces haplotypes that emulate real sequencing data with respect to the total number of variants, allele frequency spectrum, haplotype structure, and variant annotation.
	"""
	
	homepage = "https://github.com/meganmichelle/RAREsim"
	bioc = "RAREsim" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RAREsim_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RAREsim/RAREsim_1.6.0.tar.gz"]

	version("1.6.0", sha256="8fb2a823bf1b18ea70eb886ed8726c47896ac240156499e90943fd36f1de213f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
