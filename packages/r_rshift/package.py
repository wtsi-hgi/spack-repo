# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRshift(RPackage):
	"""Paleoecology Functions for Regime Shift Analysis

	Contains a variety of functions, based around
    regime shift analysis of paleoecological data.
    Citations:
    Rodionov() from Rodionov (2004) <doi:10.1029/2004GL019448>
    Lanzante() from Lanzante (1996) <doi:10.1002/(SICI)1097-0088(199611)16:11%3C1197::AID-JOC89%3E3.0.CO;2-L>
    Hellinger_trans from Numerical Ecology, Legendre & Legendre (ISBN 9780444538680)
    rolling_autoc from Liu, Gao & Wang (2018) <doi:10.1016/j.scitotenv.2018.06.276>
    Sample data sets lake_data & lake_RSI processed from Bush, Silman & Urrego (2004) <doi:10.1126/science.1090795>
    Sample data set January_PDO from NOAA: <https://www.ncei.noaa.gov/access/monitoring/pdo/>.
	"""
	
	homepage = "https://github.com/alexhroom/rshift"
	cran = "rshift" 

	version("3.0.0", md5="8c5a0c50fe0fb4c46f20f409b130d77d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
