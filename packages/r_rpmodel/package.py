# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpmodel(RPackage):
	"""P-Model

	Implements the P-model 
  (Stocker et al., 2020 <doi:10.5194/gmd-13-1545-2020>),
  predicting acclimated parameters of the enzyme kinetics of C3 photosynthesis,
  assimilation, and dark respiration rates as a function of the environment
  (temperature, CO2, vapour pressure deficit, light, atmospheric pressure).
	"""
	
	homepage = "https://github.com/stineb/rpmodel"
	cran = "rpmodel" 

	version("1.2.0", md5="ee1640ad298499185b023a207439499d")

	depends_on("r@3.6:", type=("build", "run"))
