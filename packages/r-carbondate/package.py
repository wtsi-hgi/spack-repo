# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarbondate(RPackage):
	"""Calibration and Summarisation of Radiocarbon Dates

	
  Performs Bayesian non-parametric calibration of multiple related radiocarbon determinations, and summarises the calendar age information to plot their joint calendar age density (see Heaton (2022) <doi:10.1111/rssc.12599>). 
  Also models the occurrence of radiocarbon samples as a variable-rate (inhomogeneous) Poisson process, plotting the posterior estimate for the occurrence rate of the samples over calendar time, and providing information about potential change points.
	"""
	
	homepage = "https://github.com/TJHeaton/carbondate"
	cran = "carbondate" 

	version("1.0.1", md5="90025fe5a60b6d53c21e51dd8b5f8615")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
