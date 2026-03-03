# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsfd(RPackage):
	"""Output Space-Filling Design

	A method to generate a design in the input space that sequentially fills the output space of a black-box function. The output space-filling design will be helpful in inverse design or feature-based modeling problem. 
             Please see Wang et al.(2023) <DOI:10.48550/arXiv.2305.07202> for details. This work is supported by U.S. National Foundation grant CMMI-1921646.
	"""
	
	cran = "OSFD" 

	version("1.0", md5="6269d075b5d7422aea7f3cfef5ed61ca")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-twinning", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
