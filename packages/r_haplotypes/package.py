# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaplotypes(RPackage):
	"""Manipulating DNA Sequences and Estimating Unambiguous Haplotype
Network with Statistical Parsimony

	Provides S4 classes and methods for reading and manipulating aligned DNA sequences, supporting an indel coding methods (only simple indel coding method is available in the current version), showing base substitutions and indels, calculating absolute pairwise distances between DNA sequences, and collapses identical DNA sequences into haplotypes or inferring haplotypes using user provided absolute pairwise character difference matrix.  This package also includes S4 classes and methods for estimating genealogical relationships among haplotypes using statistical parsimony and plotting parsimony networks.  
	"""
	
	homepage = "https://cran.r-project.org"
	cran = "haplotypes" 

	version("1.1.3.1", md5="c9c167831e150d1df79e86bd4f233808")

	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
