# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPinnacleData(RPackage):
	"""Market Odds Data from Pinnacle

	Market odds from from Pinnacle, an online sports betting bookmaker (see <https://www.pinnacle.com> for more information). Included are datasets for the Major League Baseball (MLB) 2016 season and the USA election 2016. These datasets can be used to build models and compare statistical information with the information from prediction markets.The Major League Baseball (MLB) 2016 dataset can be used for sabermetrics analysis and also can be used in conjunction with other popular Major League Baseball (MLB) datasets such as Retrosheets or the Lahman package by merging by GameID.
	"""
	
	homepage = "https://github.com/marcoblume/pinnacle.data"
	cran = "pinnacle.data" 

	version("0.1.4", md5="bd0e61f0b0fa79405c7b3d37dd113d15")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
