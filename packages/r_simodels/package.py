# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimodels(RPackage):
	"""Flexible Framework for Developing Spatial Interaction Models

	Develop spatial interaction models (SIMs).  SIMs predict the
    amount of interaction, for example number of trips per day, between
    geographic entities representing trip origins and destinations.
    Contains functions for creating origin-destination datasets
    from geographic input datasets and calculating movement between
    origin-destination pairs with constrained, production-constrained,
    and attraction-constrained models (Wilson 1979) <doi:10.1068/a030001>.
	"""
	
	homepage = "https://github.com/robinlovelace/simodels"
	cran = "simodels" 

	version("0.0.5", md5="dd57de06c0a5fde21d236686923b3403")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-od@0.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
