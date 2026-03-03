# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXpose(RPackage):
	"""Diagnostics for Pharmacometric Models

	Diagnostics for non-linear mixed-effects (population) 
    models from 'NONMEM' <https://www.iconplc.com/solutions/technologies/nonmem/>. 
    'xpose' facilitates data import, creation of numerical run summary 
    and provide 'ggplot2'-based graphics for data exploration and model 
    diagnostics.
	"""
	
	homepage = "https://uupharmacometrics.github.io/xpose/"
	cran = "xpose" 

	version("0.4.18", md5="b55a0065879850029d6c1caba5d5f907")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-ggforce@0.2:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-readr@2.1:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@2.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
	depends_on("r-vpc@1.1:", type=("build", "run"))
