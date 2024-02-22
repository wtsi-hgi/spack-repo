# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpseq(RPackage):
	"""Design Clinical Trials using Sequential Predictive Probability
Monitoring

	Functions are available to calibrate designs over a range of posterior and predictive thresholds, to plot the various design options, and to obtain the operating characteristics of optimal accuracy and optimal efficiency designs.
	"""
	
	homepage = "https://github.com/zabore/ppseq"
	cran = "ppseq" 

	version("0.2.3", md5="784b16bc83f0c72989716ce012aad5d6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
