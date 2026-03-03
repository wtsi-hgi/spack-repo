# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSptm(RPackage):
	"""SemiParametric Transformation Model Methods

	Implements semiparametric transformation model two-phase estimation using calibration weights. The method in Fong and Gilbert (2015) Calibration weighted estimation of semiparametric transformation models for two-phase sampling. Statistics in Medicine <DOI:10.1002/sim.6439>.
	"""
	
	cran = "sptm" 

	version("2019.11-25", md5="92fe4c67a7897e9405588efb3945f70c")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-kyotil", type=("build", "run"))
