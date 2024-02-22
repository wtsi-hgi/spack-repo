# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypetools(RPackage):
	"""Tools for Processing and Analyzing Files from the Hydrological
Catchment Model HYPE

	Work with model files (setup, input, output) from
    the hydrological catchment model HYPE: Streamlined file import and export, standard 
    evaluation plot routines, diverse post-processing and aggregation routines 
    for hydrological model analysis.
	"""
	
	homepage = "https://hypeweb.smhi.se/"
	cran = "HYPEtools" 

	version("1.6.1", md5="00e3d1b70e2ed9adfa1b18b4dc3846e7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
