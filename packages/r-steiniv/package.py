# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSteiniv(RPackage):
	"""Semi-Parametric Stein-Like Estimator with Instrumental Variables

	Routines for computing different types of linear estimators, based on instrumental variables (IVs), including the semi-parametric Stein-like (SPS) estimator, originally introduced by Judge and Mittelhammer (2004)  <DOI:10.1198/016214504000000430>. 
	"""
	
	homepage = "https://cran.r-project.org/package=SteinIV"
	cran = "SteinIV" 

	version("0.1-1", md5="a5da3df39cea234020d2d93b93ea2637")

	depends_on("r@2.10.1:", type=("build", "run"))
