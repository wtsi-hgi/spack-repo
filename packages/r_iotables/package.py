# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIotables(RPackage):
	"""Reproducible Input-Output Economics Analysis, Economic and
Environmental Impact Assessment with Empirical Data

	Pre-processing and basic analytical tasks related to working
    with Eurostat's symmetric input-output tables and provide basic
    input-output economics calculations. The package is part of rOpenGov
    <http://ropengov.github.io/> to open source open government initiatives.
	"""
	
	homepage = "https://iotables.dataobservatory.eu/"
	cran = "iotables" 

	version("0.9.3", md5="eed960a9914965c11dc867e513b295c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-eurostat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
