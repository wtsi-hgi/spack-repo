# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReldists(RPackage):
	"""Estimation for some Reliability Distributions

	Parameters estimation and linear regression models for Reliability 
    distributions families reviewed by Almalki & Nadarajah (2014)
    <doi:10.1016/j.ress.2013.11.010> using Generalized Additive
    Models for Location, Scale and Shape, aka GAMLSS by Rigby & Stasinopoulos
    (2005) <doi:10.1111/j.1467-9876.2005.00510.x>.
	"""
	
	homepage = "https://ousuga.github.io/RelDists/"
	cran = "RelDists" 

	version("1.0.0", md5="ba7a94480e4c37332025b05ffbc3d959")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-estimationtools@4:", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-zipfr", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-lamw", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
