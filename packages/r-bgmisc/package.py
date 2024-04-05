# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgmisc(RPackage):
	"""An R Package for Extended Behavior Genetics Analysis

	The BGmisc R package offers a comprehensive suite of
    functions tailored for extended behavior genetics analysis, including
    model identification, calculating relatedness, pedigree conversion,
    pedigree simulation, and more.
	"""
	
	homepage = "https://github.com/R-Computing-Lab/BGmisc/"
	cran = "BGmisc" 

	version("1.2.0", md5="a0d7df985cd850285ec7ecac7ba2c7b7")
	version("1.0.1", md5="79cd771d8a515fc2abb897f22acb5ba0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
