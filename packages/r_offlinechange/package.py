# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROfflinechange(RPackage):
	"""Detect Multiple Change Points from Time Series

	Detect the number and locations of change points. The locations can be either exact or in terms of ranges, 
            depending on the available computational resource. The method is based on Jie Ding, Yu Xiang, Lu Shen, Vahid Tarokh (2017) <doi:10.1109/TSP.2017.2711558>.
	"""
	
	cran = "offlineChange" 

	version("0.0.4", md5="a803ffb9a4f418c0ed375d4c672b05b2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
