# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpicurve(RPackage):
	"""Plot an Epidemic Curve

	Creates simple or stacked epidemic curves for hourly, daily, weekly or monthly outcome data.
	"""
	
	homepage = "https://github.com/IamKDO/EpiCurve"
	cran = "EpiCurve" 

	version("2.4-2", md5="a49ddb3ff96f65d50643e70f0d36408a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-isoweek", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
