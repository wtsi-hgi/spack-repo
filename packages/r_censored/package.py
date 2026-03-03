# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensored(RPackage):
	"""'parsnip' Engines for Survival Models

	Engines for survival models from the 'parsnip' package. These
    include parametric models (e.g., Jackson (2016)
    <doi:10.18637/jss.v070.i08>), semi-parametric (e.g., Simon et al
    (2011) <doi:10.18637/jss.v039.i05>), and tree-based models (e.g.,
    Buehlmann and Hothorn (2007) <doi:10.1214/07-STS242>).
	"""
	
	homepage = "https://github.com/tidymodels/censored"
	cran = "censored" 

	version("0.3.0", md5="8761e89d295327c0d3cf7e0aa2f2b4b9")

	depends_on("r-parsnip@1.1:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival@3.3.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat@1.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-prodlim@2023.3.31:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble@3.1.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
