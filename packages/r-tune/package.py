# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTune(RPackage):
	"""Tidy Tuning Tools

	The ability to tune models is important. 'tune' contains
    functions and classes to be used in conjunction with other
    'tidymodels' packages for finding reasonable values of
    hyper-parameters in models, pre-processing methods, and
    post-processing steps.
	"""
	
	homepage = "https://tune.tidymodels.org/"
	cran = "tune" 

	version("1.1.2", md5="e622a0b09c20417a6e681e79ed2c1f0e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-dials@1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-gpfit", type=("build", "run"))
	depends_on("r-hardhat@1.2:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-parsnip@1.0.2:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-recipes@1.0.4:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-rsample@1.2:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.6.1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-workflows@1:", type=("build", "run"))
	depends_on("r-yardstick@1:", type=("build", "run"))
