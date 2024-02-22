# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolycor(RPackage):
	"""Polychoric and Polyserial Correlations

	Computes polychoric and polyserial correlations by quick "two-step" methods or ML, 
  optionally with standard errors; tetrachoric and biserial correlations are special cases.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/polycor/"
	cran = "polycor" 

	version("0.8-1", md5="bcf23e352787794c7e36875d6cd8d6f6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-admisc@0.22:", type=("build", "run"))
