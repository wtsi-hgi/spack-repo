# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaconvert(RPackage):
	"""An Automatic Suite for Estimation of Various Effect Size
Measures

	Automatically estimate 11 effect size measures from a well-formatted dataset. Various other functions can help, for example, removing dependency between several effect sizes, or identifying differences between two datasets.
    This package is mainly designed to assist in conducting a systematic review with a meta-analysis but can be useful to any researcher interested in estimating an effect size. 
	"""
	
	cran = "metaConvert" 

	version("1.0.0", md5="a4bd88cee70bfcaed03a1ba1eea2243d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-comparedf", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-estimraw", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
