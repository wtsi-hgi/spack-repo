# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwofost(RPackage):
	"""WOFOST Crop Growth Simulation Model

	An implementation of the WOFOST ("World Food Studies") crop growth model. WOFOST is a dynamic simulation model that uses daily weather data, and crop, soil and management parameters to simulate crop growth and development. See De Wit et al. (2019) <doi:10.1016/j.agsy.2018.06.018> for a recent review of the history and use of the model.
	"""
	
	homepage = "https://CRAN.R-project.org/package=Rwofost"
	cran = "Rwofost" 

	version("0.8-3", md5="c67c176af5739b79145b34fd2de5de68")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-meteor", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
