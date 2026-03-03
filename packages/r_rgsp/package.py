# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgsp(RPackage):
	"""Repetitive Group Sampling Plan Based on Cpk

	Functions to calculate Sample Number and Average Sample Number for Repetitive Group Sampling Plan Based on Cpk as given in Aslam et al. (2013) (<DOI:10.1080/00949655.2012.663374>).
	"""
	
	homepage = "https://github.com/myaseen208/rgsp"
	cran = "rgsp" 

	version("0.2.0", md5="368f97559199cfd0a1e2c157aa40940d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
