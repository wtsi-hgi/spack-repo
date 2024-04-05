# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYardstick(RPackage):
	"""Tidy Characterizations of Model Performance

	Tidy tools for quantifying how well model fits to a data set
    such as confusion matrices, class probability curve summaries, and
    regression metrics (e.g., RMSE).
	"""
	
	homepage = "https://github.com/tidymodels/yardstick"
	cran = "yardstick" 

	version("1.3.1", md5="5e35a7fabd9e7ec8effd168556c67753")
	version("1.3.0", md5="1cf92ed73945340367924fb3a8c7bdeb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-hardhat@1.3:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
