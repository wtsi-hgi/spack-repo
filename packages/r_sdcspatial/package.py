# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdcspatial(RPackage):
	"""Statistical Disclosure Control for Spatial Data

	Privacy protected raster maps 
  can be created from spatial point data. Protection
  methods include smoothing of dichotomous variables by de Jonge and de Wolf (2016) 
  <doi:10.1007/978-3-319-45381-1_9>, continuous variables by de Wolf and 
  de Jonge (2018) <doi:10.1007/978-3-319-99771-1_23>, suppressing 
  revealing values and a generalization of the quad tree method by 
  Suñé, Rovira, Ibáñez and Farré (2017) <doi:10.2901/EUROSTAT.C2017.001>.
	"""
	
	homepage = "https://github.com/edwindj/sdcSpatial"
	cran = "sdcSpatial" 

	version("0.5.2", md5="944ae0279c282e81a99afdd655c88e3f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
