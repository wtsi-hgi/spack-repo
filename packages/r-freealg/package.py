# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreealg(RPackage):
	"""The Free Algebra

	The free algebra in R with non-commuting indeterminates.
     Uses 'disordR' discipline
     (Hankin, 2022, <doi:10.48550/ARXIV.2210.03856>).  To cite the
     package in publications please use Hankin (2022)
     <doi:10.48550/ARXIV.2211.04002>.
	"""
	
	homepage = "https://github.com/RobinHankin/freealg"
	cran = "freealg" 

	version("1.1-1", md5="029d27fce8887c22a13b58a96507d7f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-partitions@1.9.22:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-disordr@0.9:", type=("build", "run"))
