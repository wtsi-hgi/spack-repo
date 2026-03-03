# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatgenibd(RPackage):
	"""Calculation of IBD Probabilities

	For biparental, three and four-way crosses Identity by Descent 
    (IBD) probabilities can be calculated using Hidden Markov Models and 
    inheritance vectors following Lander and Green
    (<https://www.jstor.org/stable/29713>) and Huang
    (<doi:10.1073/pnas.1100465108>). One of a series of statistical genetic 
    packages for streamlining the analysis of typical plant breeding experiments
    developed by Biometris.
	"""
	
	homepage = "https://biometris.github.io/statgenIBD/index.html"
	cran = "statgenIBD" 

	version("1.0.7", md5="66de522bd6926a9c7b2ada5fdde39ab2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-statgengwas@1.0.9:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
