# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialregimes(RPackage):
	"""Spatial Constrained Clusterwise Regression

	A collection of functions for estimating spatial regimes, aggregations of neighboring spatial units that are homogeneous in functional terms. The term spatial regime, therefore, should not be understood as a synonym for cluster. More precisely, the term cluster does not presuppose any functional relationship between the variables considered, while the term regime is linked to a regressive relationship underlying the spatial process. 
	"""
	
	cran = "SpatialRegimes" 

	version("1.1", md5="af1e04075ac32d9df069df47aa6f9240")

	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-gwmodel", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
