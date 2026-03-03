# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTssim(RPackage):
	"""Simulation of Daily and Monthly Time Series

	Flexible simulation of time series using time
    series components, including seasonal, calendar and outlier effects.
    Algorithm described in Ollech, D. (2021) <doi:10.1515/jtse-2020-0028>.
	"""
	
	cran = "tssim" 

	version("0.1.7", md5="76b3800482ef7039ac0ba263e70ba226")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-dsa", type=("build", "run"))
	depends_on("r-tsbox", type=("build", "run"))
