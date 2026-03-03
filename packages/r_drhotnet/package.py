# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrhotnet(RPackage):
	"""Differential Risk Hotspots in a Linear Network

	Performs the identification of differential risk hotspots (Briz-Redon et al. 2019) <doi:10.1016/j.aap.2019.105278> along a linear network. Given a marked point pattern lying on the linear network, the method implemented uses a network-constrained version of kernel density estimation (McSwiggan et al. 2017) <doi:10.1111/sjos.12255> to approximate the probability of occurrence across space for the type of event specified by the user through the marks of the pattern (Kelsall and Diggle 1995) <doi:10.2307/3318678>. The goal is to detect microzones of the linear network where the type of event indicated by the user is overrepresented.
	"""
	
	cran = "DRHotNet" 

	version("2.3", md5="ff1f5ec0a45f0dbab2d2d7c26a1872d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pbsmapping", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-linnet", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
