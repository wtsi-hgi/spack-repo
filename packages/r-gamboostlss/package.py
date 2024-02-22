# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamboostlss(RPackage):
	"""Boosting Methods for 'GAMLSS'

	Boosting models for fitting generalized additive models for
  location, shape and scale ('GAMLSS') to potentially high dimensional
  data.
	"""
	
	homepage = "For"
	cran = "gamboostLSS" 

	version("2.0-7", md5="dce81b5eb7c880c303fb7b1e7a5f8fdf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mboost@2.8.0:", type=("build", "run"))
	depends_on("r-stabs@0.5.0:", type=("build", "run"))
