# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetrology(RPackage):
	"""Support for Metrological Applications

	Provides classes and calculation and plotting functions 
 for metrology applications, including measurement uncertainty estimation
 and inter-laboratory metrology comparison studies. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/metrology/"
	cran = "metRology" 

	version("0.9-28-1", md5="effb94601c66e7fe520d77c8cc816dc8")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
