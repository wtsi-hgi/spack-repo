# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicsprint(RPackage):
	"""Cross omic genetic fingerprinting

	omicsPrint provides functionality for cross omic genetic fingerprinting, for example, to verify sample relationships between multiple omics data types, i.e. genomic, transcriptomic and epigenetic (DNA methylation).
	"""
	
	bioc = "omicsPrint"

	version("1.28.0", commit="ab1abddfb13676808553ded27533b6f5c9243c45")
	version("1.22.0", commit="25859e6993508a5250f41017e5f63883a5fdf2e1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
