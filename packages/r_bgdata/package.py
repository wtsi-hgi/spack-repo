# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgdata(RPackage):
	"""A Suite of Packages for Analysis of Big Genomic Data

	An umbrella package providing a phenotype/genotype data structure
    and scalable and efficient computational methods for large genomic datasets
    in combination with several other packages: 'BEDMatrix', 'LinkedMatrix',
    and 'symDMatrix'.
	"""
	
	homepage = "https://github.com/QuantGen/BGData"
	cran = "BGData" 

	version("2.4.1", md5="1125e154d6230ecf49d71fd6194271d5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-bedmatrix@1.4:", type=("build", "run"))
	depends_on("r-linkedmatrix@1.3:", type=("build", "run"))
	depends_on("r-symdmatrix@2:", type=("build", "run"))
	depends_on("r-crochet@2.1:", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-synchronicity", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-bit", type=("build", "run"))
