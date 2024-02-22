# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkimr(RPackage):
	"""Compact and Flexible Summaries of Data

	A simple to use summary function that can be used with pipes
    and displays nicely in the console. The default summary statistics may
    be modified by the user as can the default formatting.  Support for
    data frames and vectors is included, and users can implement their own
    skim methods for specific object types as described in a vignette.
    Default summaries include support for inline spark graphs.
    Instructions for managing these on specific operating systems are
    given in the "Using skimr" vignette and the README.
	"""
	
	homepage = "https://docs.ropensci.org/skimr/"
	cran = "skimr" 

	version("2.1.5", md5="3f8a61ba5a88a3e51ec813d18e5fa814")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-knitr@1.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-pillar@1.6.4:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-repr", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-stringr@1.1:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
