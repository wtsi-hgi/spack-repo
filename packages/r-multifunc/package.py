# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultifunc(RPackage):
	"""Analysis of Ecological Drivers on Ecosystem Multifunctionality

	Methods for the analysis of how ecological drivers affect the
    multifunctionality of an ecosystem based on methods of Byrnes et al. 
    2016 <doi:10.1111/2041-210X.12143> and Byrnes et al. 
    2022 <doi:10.1101/2022.03.17.484802>. Most standard
    methods in the literature are implemented (see vignettes) in a tidy
    format.
	"""
	
	homepage = "https://jebyrnes.github.io/multifunc/"
	cran = "multifunc" 

	version("0.9.4", md5="02da5ecaddb34f75e60281550969b2c9")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
