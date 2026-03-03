# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQqplotr(RPackage):
	"""Quantile-Quantile Plot Extensions for 'ggplot2'

	Extensions of 'ggplot2' Q-Q plot functionalities.
	"""
	
	homepage = "https://github.com/aloy/qqplotr"
	cran = "qqplotr" 

	version("0.0.6", md5="38ab3b831917a4f1b2fdb2b722e0195b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-opdisdownsampling", type=("build", "run"))
	depends_on("r-qqconf@1.3.1:", type=("build", "run"))
