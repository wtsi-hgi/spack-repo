# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimstudy(RPackage):
	"""Simulation of Study Data

	Simulates data sets in order to explore modeling
    techniques or better understand data generating processes. The user
    specifies a set of relationships between covariates, and generates
    data based on these specifications. The final data sets can represent
    data from randomized control trials, repeated measure (longitudinal)
    designs, and cluster randomized trials. Missingness can be generated
    using various mechanisms (MCAR, MAR, NMAR).
	"""
	
	homepage = "https://github.com/kgoldfeld/simstudy"
	cran = "simstudy" 

	version("0.7.1", md5="be296d11e6690877131610d41de6dcff")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-fastglm", type=("build", "run"))
	depends_on("r-pbv@0.4.22:", type=("build", "run"))
