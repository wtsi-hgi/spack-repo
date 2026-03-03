# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalscore(RPackage):
	"""Package for Sequence Analysis by Local Score

	Functionalities for calculating the local score and calculating statistical relevance (p-value) to find a local Score in a sequence of given distribution (S. Mercier and J.-J. Daudin (2001) <https://hal.science/hal-00714174/>) ; S. Karlin and S. Altschul (1990) <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC53667/>  ; S. Mercier, D. Cellier and F. Charlot (2003) <https://hal.science/hal-00937529v1/> ; A. Lagnoux, S. Mercier and P. Valois (2017) <doi:10.1093/bioinformatics/btw699> ).
	"""
	
	cran = "localScore" 

	version("1.0.11", md5="f4d73c5aff1910b2c45024f03c537e20")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
