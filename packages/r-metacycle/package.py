# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetacycle(RPackage):
	"""Evaluate Periodicity in Large Scale Data

	There are two functions-meta2d and meta3d for
    detecting rhythmic signals from time-series datasets. For analyzing
    time-series datasets without individual information, 'meta2d' is 
    suggested, which could incorporates multiple methods from ARSER, 
    JTK_CYCLE and Lomb-Scargle in the detection of interested rhythms. For 
    analyzing time-series datasets with individual information, 'meta3d' is 
    suggested, which takes use of any one of these three methods to analyze 
	time-series data individual by individual and gives out integrated values 
    based on analysis result of each individual.
	"""
	
	cran = "MetaCycle" 

	version("1.2.0", md5="70190ab28f2c81008336327264431f8f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-gnm", type=("build", "run"))
