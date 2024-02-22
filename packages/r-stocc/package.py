# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStocc(RPackage):
	"""Fit a Spatial Occupancy Model via Gibbs Sampling

	Fit a spatial-temporal occupancy models using
    a probit formulation instead of a traditional logit
    model.
	"""
	
	cran = "stocc" 

	version("1.31", md5="e0f8cf1b29033f9386d35a92f88deb91")

	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
