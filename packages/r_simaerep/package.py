# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimaerep(RPackage):
	"""Find Clinical Trial Sites Under-Reporting Adverse Events

	Monitoring of Adverse Event (AE) reporting in clinical trials is 
  important for patient safety. Sites that are under-reporting AEs can be detected 
  using Bootstrap-based simulations that simulate overall AE reporting. Based on the 
  simulation an AE under-reporting probability is assigned to each site in a 
  given trial (Koneswarakantha 2021 <doi:10.1007/s40264-020-01011-5>).
	"""
	
	homepage = "https://openpharma.github.io/simaerep/"
	cran = "simaerep" 

	version("0.5.0", md5="e269292574643cc18a2bbcc3ed802b37")
	version("0.4.3", md5="71b082cc2fd3173c2519c9b80cfba75f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-furrr@0.2.1:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
