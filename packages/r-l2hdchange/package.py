# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL2hdchange(RPackage):
	"""L2 Inference for Change Points in High-Dimensional Time Series

	Provides a method for detecting multiple change points in high-dimensional time
    series, targeting dense or spatially clustered signals. See Li et al. (2023) 
    "L2 Inference for Change Points in High-Dimensional Time Series via a Two-Way MOSUM". 
    arXiv preprint <arXiv:2208.13074>.
	"""
	
	cran = "L2hdchange" 

	version("1.0", md5="48105cdf5b27f01cf023f476a2142455")

	depends_on("r@2.10:", type=("build", "run"))
