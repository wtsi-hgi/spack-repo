# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynatopgis(RPackage):
	"""Algorithms for Helping Build Dynamic TOPMODEL Implementations
from Spatial Data

	A set of algorithms based on Quinn et al. (1991) <doi:10.1002/hyp.3360050106> for processing river network and digital elevation data to build implementations of Dynamic TOPMODEL, a semi-distributed hydrological model proposed in Beven and Freer (2001) <doi:10.1002/hyp.252>. The 'dynatop' package implements simulation code for Dynamic TOPMODEL based on the output of 'dynatopGIS'.
	"""
	
	homepage = "https://waternumbers.github.io/dynatopGIS/"
	cran = "dynatopGIS" 

	version("0.2.5", md5="732b62b8f8419a2b272d3e77d83de484")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
