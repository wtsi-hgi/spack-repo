# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialvx(RPackage):
	"""Spatial Forecast Verification

	Spatial forecast verification refers to verifying weather forecasts when the verification set (forecast and observations) is on a spatial field, usually a high-resolution gridded spatial field.  Most of the functions here require the forecast and observed fields to be gridded and on the same grid. For a thorough review of most of the methods in this package, please see Gilleland et al. (2009) <doi: 10.1175/2009WAF2222269.1> and for a tutorial on some of the main functions available here, see Gilleland (2022) <doi: 10.5065/4px3-5a05>. 
	"""
	
	homepage = "https://projects.ral.ucar.edu/icp/SpatialVx/"
	cran = "SpatialVx" 

	version("1.0-2", md5="9949ef4dc22d6812e420bdcf187f7e4e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-fields@6.8:", type=("build", "run"))
	depends_on("r-smoothie", type=("build", "run"))
	depends_on("r-smatr", type=("build", "run"))
	depends_on("r-turboem", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-linnet", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-distillery", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
