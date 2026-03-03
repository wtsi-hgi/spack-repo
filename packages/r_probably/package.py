# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbably(RPackage):
	"""Tools for Post-Processing Predicted Values

	Models can be improved by post-processing class
    probabilities, by: recalibration, conversion to hard probabilities,
    assessment of equivocal zones, and other activities. 'probably'
    contains tools for conducting these operations as well as calibration
    tools and conformal inference techniques for regression models.
	"""
	
	homepage = "https://github.com/tidymodels/probably"
	cran = "probably" 

	version("1.0.3", md5="8bf79618fd6bfe3a51188616a3424aad")
	version("1.0.2", md5="f4607f747f783c3a488ccd9c9d6ee199")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-butcher", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-generics@0.1.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.2:", type=("build", "run"))
	depends_on("r-tune@1.1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.4.1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-workflows@1.1.4:", type=("build", "run"))
	depends_on("r-yardstick@1.3:", type=("build", "run"))
