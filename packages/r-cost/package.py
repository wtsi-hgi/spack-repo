# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCost(RPackage):
	"""Copula-Based Semiparametric Models for Spatio-Temporal Data

	Parameter estimation, one-step ahead forecast and new location
    prediction methods for spatio-temporal data.
	"""
	
	cran = "COST" 

	version("0.1.0", md5="31bfdf9d0b0a0282fc8cad99be3f6d0d")

	depends_on("r-copula", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
