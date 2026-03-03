# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvpresmooth(RPackage):
	"""Presmoothed Estimation in Survival Analysis

	Presmoothed estimators of survival, density, cumulative and non-cumulative hazard functions with right-censored survival data. For details, see Lopez-de-Ullibarri and Jacome (2013) <doi:10.18637/jss.v054.i11>.
	"""
	
	cran = "survPresmooth" 

	version("1.1-11", md5="5ad1dc74295f383c18b8b9d285592c21")

	depends_on("r@3.0.1:", type=("build", "run"))
