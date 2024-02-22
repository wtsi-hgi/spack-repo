# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdi(RPackage):
	"""Phenotypic Index Measures for Oak Decline Severity

	Oak declines are complex disease syndromes and consist of many visual indicators that include aspects of tree size, crown condition and trunk condition. This can cause difficulty in the manual classification of symptomatic and non-symptomatic trees from what is in reality a broad spectrum of oak tree health condition. Two phenotypic oak decline indexes have been developed to quantitatively describe and differentiate oak decline syndromes in Quercus robur. This package provides a toolkit to generate these decline indexes from phenotypic descriptors using the machine learning algorithm random forest. The methodology for generating these indexes is outlined in Finch et al. (2121) <doi:10.1016/j.foreco.2021.118948>.
	"""
	
	homepage = "https://jasenfinch.github.io/pdi"
	cran = "pdi" 

	version("0.4.2", md5="efb6fa2c3198af0a101b923806bb2009")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
