# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoissonmt(RPackage):
	"""Robust M-Estimators Based on Transformations for Poisson Model

	R functions for the computation of Least Square based on transformation (L2T) and robust M-estimators based on transformations (MT-estimators) for Poisson regression models.
	"""
	
	cran = "poissonMT" 

	version("0.3-5", md5="778130476dd3fb4cfb39697cd422bc54")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-robcbi", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
