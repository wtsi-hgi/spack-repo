# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenmodel(RPackage):
	"""Insect Phenology Model Evaluation Based on Daily Temperatures

	Generates predicted stage change days for an insect, based on daily temperatures and development rate parameters, as developed by Pollard (2014) <http://mural.maynoothuniversity.ie/view/ethesisauthor/Pollard=3ACiaran_P=2E=3A=3A.html>. A few example datasets are included and implemented for P. vulgatissima, the blue willow beetle, but the approach can be readily applied to other species that display similar behaviour.
	"""
	
	cran = "phenModel" 

	version("1.0", md5="05e7a591719474a6987e4286335c7a26")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
