# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWats(RPackage):
	"""Wrap Around Time Series Graphics

	Wrap-around Time Series (WATS) plots for interrupted time series
    designs with seasonal patterns.
    Longitudinal trajectories are shown in both Cartesian and polar coordinates.
    In many scenarios, a WATS plot more clearly shows the existence and effect size of
    of an intervention.
    This package accompanies
    "Graphical Data Analysis on the Circle: Wrap-Around Time Series Plots for (Interrupted) Time Series Designs"
    by Rodgers, Beasley, & Schuelke (2014)
    <doi:10.1080/00273171.2014.946589>;
    see 'citation("Wats")' for details.
	"""
	
	homepage = "https://ouhscbbmc.github.io/Wats/"
	cran = "Wats" 

	version("1.0.1", md5="25b580cc4d31695838da93d48e8f78c4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
