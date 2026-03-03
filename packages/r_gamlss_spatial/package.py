# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssSpatial(RPackage):
	"""Spatial Terms in Generalized Additive Models for Location Scale
and Shape Models

	It allows us to fit Gaussian Markov Random Field within the
    Generalized Additive Models for Location Scale and Shape algorithms.
	"""
	
	homepage = "https://www.gamlss.com/"
	cran = "gamlss.spatial" 

	version("3.0-2", md5="dbdc89caadb7c55d3590353ff4ac6a96")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-gamlss@4.2.7:", type=("build", "run"))
	depends_on("r-gamlss-add", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
