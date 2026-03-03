# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrodcindex(RPackage):
	"""Duration Curve Hydrological Model Indexes

	Compute duration curves of daily flow series, both real and modeled, to be compared through indexes of flow duration curves. The package functions include comparative plots and goodness of fit tests. Flow duration curve indexes are based on: Yilmaz et al., (2008) <DOI:10.1029/2007WR006716>.
	"""
	
	cran = "hydroDCindex" 

	version("1.0.0", md5="f1d864685c61c8bb919a27b7dbe33b77")

	depends_on("r@2.10:", type=("build", "run"))
