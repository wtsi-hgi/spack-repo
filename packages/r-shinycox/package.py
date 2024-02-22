# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinycox(RPackage):
	"""Create 'shiny' Applications for Cox Proportional Hazards Models

	Takes one or more fitted Cox proportional hazards models and writes
    a 'shiny' application to a directory specified by the user. The 'shiny' 
    application displays predicted survival curves based on user input, and 
    contains none of the original data used to create the Cox model or models. 
    The goal is towards visualization and presentation of predicted survival
    curves.
	"""
	
	homepage = "https://github.com/harryc598/shinyCox"
	cran = "shinyCox" 

	version("1.0.1", md5="e735f43f5939897e1a4cdfa3afdc46ba")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-survival@3.3:", type=("build", "run"))
