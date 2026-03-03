# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REd50simulation(RPackage):
	"""Estimate ED50 and Its Confidence Interval

	Functions of five estimation method for ED50 (50 percent effective dose) are provided, and they are respectively
    Dixon-Mood method (1948) <doi:10.2307/2280071>, Choi's original turning point method (1990) <doi:10.2307/2531453> and it's modified version given by
    us, as well as logistic regression and isotonic regression. Besides, the package also supports
    comparison between two estimation results.
	"""
	
	cran = "ed50simulation" 

	version("0.1.1", md5="953380d0585bc668a2e0ceb50f3c625e")

	depends_on("r-boot", type=("build", "run"))
