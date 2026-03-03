# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiplencc(RPackage):
	"""Weighted Cox-Regression for Nested Case-Control Data

	Fit Cox proportional hazard models with a weighted 
  partial likelihood. It handles one or multiple endpoints, additional matching 
  and makes it possible to reuse controls for other endpoints 
  Stoer NC and Samuelsen SO (2016) <doi:10.32614/rj-2016-030>.
	"""
	
	cran = "multipleNCC" 

	version("1.2-4", md5="c689d2dbe671aeff2e559da17b7ebb1a")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
