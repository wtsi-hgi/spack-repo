# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKrige(RPackage):
	"""Geospatial Kriging with Metropolis Sampling

	Estimates kriging models for geographical point-referenced data. Method is described in Gill (2020) <doi:10.1177/1532440020930197>.
	"""
	
	cran = "krige" 

	version("0.6.2", md5="2d8cb7927e852f93926b8a0a912f19d8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
