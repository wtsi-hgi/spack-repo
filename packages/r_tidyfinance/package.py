# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyfinance(RPackage):
	"""Tidy Finance Helper Functions

	Helper functions for empirical research in financial economics, 
  addressing a variety of topics covered in Scheuch, Voigt, and Weiss (2023) <doi:10.1201/b23237>. 
  The package is designed to provide shortcuts for issues extensively discussed in the book, 
  facilitating easier application of its concepts. For more information and resources 
  related to the book, visit <https://www.tidy-finance.org/r/index.html>.
	"""
	
	homepage = "https://www.tidy-finance.org/r/"
	cran = "tidyfinance" 

	version("0.1.0", md5="cd6d0766e13a77a9fc46d4b1cbc9661a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-rlang@1.1.3:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-lubridate@1.9.3:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
