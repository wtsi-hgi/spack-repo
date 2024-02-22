# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeirfansy(RPackage):
	"""Extended Susceptible-Exposed-Infected-Recovery Model

	Extended Susceptible-Exposed-Infected-Recovery Model for 
    handling high false negative rate and symptom based administration of 
    diagnostic tests. <doi:10.1101/2020.09.24.20200238>.
	"""
	
	homepage = "https://github.com/umich-biostatistics/SEIRfansy"
	cran = "SEIRfansy" 

	version("1.1.1", md5="586f9e2ee2603a4801880e759483afef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
