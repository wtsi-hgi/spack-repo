# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChantrics(RPackage):
	"""Loglikelihood Adjustments for Econometric Models

	Adjusts the loglikelihood of common econometric models for
    clustered data based on the estimation process suggested in 
    Chandler and Bate (2007) <doi:10.1093/biomet/asm015>, using the 'chandwich' 
    package <https://cran.r-project.org/package=chandwich>, and provides 
    convenience functions for inference on the adjusted models. 
	"""
	
	homepage = "https://chantrics.theobruckbauer.eu"
	cran = "chantrics" 

	version("1.0.0", md5="91479e056661154bfb9452abee98114e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-chandwich", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
