# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjdqa(RPackage):
	"""Quality Assessment for Seasonal Adjustment

	Add-in to the 'RJDemetra' package on seasonal adjustments.
    It allows to produce dashboards to summarise models and quickly check the quality of the seasonal adjustment.
	"""
	
	homepage = "https://aqlt.github.io/rjdqa/"
	cran = "rjdqa" 

	version("0.1.3", md5="3c393f537255958daac60aa1bed60b06")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rjdemetra", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-ggdemetra", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
