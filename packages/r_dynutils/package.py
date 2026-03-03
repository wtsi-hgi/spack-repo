# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynutils(RPackage):
	"""Common Functionality for the 'dynverse' Packages

	
  Provides common functionality for the 'dynverse' packages. 
  'dynverse' is created to support the development, execution, and benchmarking of trajectory inference methods.
  For more information, check out <https://dynverse.org>.
	"""
	
	homepage = "https://github.com/dynverse/dynutils"
	cran = "dynutils" 

	version("1.0.11", md5="2d0fd6d9ad22f3a423fae90375d34a54")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-proxyc@0.3.3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
