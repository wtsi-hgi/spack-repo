# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgstream(RPackage):
	"""Create Streamplots in 'ggplot2'

	Make smoothed stacked area charts in 'ggplot2'. Stream plots are useful to show magnitude trends over time.
	"""
	
	cran = "ggstream" 

	version("0.1.0", md5="63facd5ad07c01c2cbaf45ce26dab75c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
