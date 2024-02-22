# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnalogue(RPackage):
	"""Analogue and Weighted Averaging Methods for Palaeoecology

	Fits Modern Analogue Technique and Weighted Averaging transfer
  	     function models for prediction of environmental data from species
	     data, and related methods used in palaeoecology.
	"""
	
	homepage = "https://github.com/gavinsimpson/analogue"
	cran = "analogue" 

	version("0.17-6", md5="f4fcf06d896fa95e76d79da19c19e6ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vegan@2.2.0:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-brglm", type=("build", "run"))
	depends_on("r-princurve@2.0.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
