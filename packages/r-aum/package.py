# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAum(RPackage):
	"""Area Under Minimum of False Positives and Negatives

	Standard template library sort is
 used to implement an efficient  
 algorithm <arXiv:2107.01285> for computing Area Under Minimum and
 directional derivatives.
	"""
	
	homepage = "https://github.com/tdhock/aum"
	cran = "aum" 

	version("2023.6.14", md5="ccc7748b7cd532499300876a22065ed4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
