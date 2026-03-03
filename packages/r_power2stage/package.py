# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPower2stage(RPackage):
	"""Power and Sample-Size Distribution of 2-Stage Bioequivalence
Studies

	Contains functions to obtain the operational characteristics of 
    bioequivalence studies in Two-Stage Designs (TSD) via simulations.
	"""
	
	homepage = "https://github.com/Detlew/Power2Stage"
	cran = "Power2Stage" 

	version("0.5-4", md5="60b89bbd54584753dcfe85d70d85337e")

	depends_on("r-powertost", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
