# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcordance(RPackage):
	"""Product Concordance

	A set of utilities for matching products in different
	     classification codes used in international trade
	     research. It supports concordance between the Harmonized
	     System (HS0, HS1, HS2, HS3, HS4, HS5, HS combined), the Standard 
	     International Trade Classification (SITC1, SITC2, SITC3, SITC4), 
	     the North American Industry Classification System (NAICS combined),
	     as well as the Broad Economic Categories (BEC), the International 
	     Standard of Industrial Classification (ISIC), and the Standard Industrial 
	     Classification (SIC). It also provides code nomenclature/descriptions 
	     look-up, Rauch classification look-up (via concordance to SITC2), and
	     trade elasticity look-up (via concordance to HS0 or SITC3
	     codes).
	"""
	
	cran = "concordance" 

	version("2.0.0", md5="78de087356969c6a6eb0664256018d12")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
