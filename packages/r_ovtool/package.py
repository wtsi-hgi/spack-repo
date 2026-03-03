# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROvtool(RPackage):
	"""Omitted Variable Tool

	This tool was designed to assess the sensitivity of research findings to omitted variables when estimating causal effects using propensity score (PS) weighting. This tool produces graphics and summary results that will enable a researcher to quantify the impact an omitted variable would have on their results. Burgette et al. (2021) describe the methodology behind the primary function in this package, ov_sim. The method is demonstrated in Griffin et al. (2020) <doi:10.1016/j.jsat.2020.108075>.
	"""
	
	cran = "OVtool" 

	version("1.0.3", md5="0435ccb229a95e76c07083d11b52230c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-twang", type=("build", "run"))
	depends_on("r-amelia", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-varhandle", type=("build", "run"))
