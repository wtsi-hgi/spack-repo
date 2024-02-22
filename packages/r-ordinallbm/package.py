# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinallbm(RPackage):
	"""Co-Clustering of Ordinal Data via Latent Continuous Random
Variables

	It implements functions for simulation and estimation of the ordinal latent block model (OLBM), as described in Corneli, Bouveyron and Latouche (2019).  
	"""
	
	cran = "ordinalLBM" 

	version("1.0", md5="46174ac2df6f6e7e5597a3bda52ee17f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
