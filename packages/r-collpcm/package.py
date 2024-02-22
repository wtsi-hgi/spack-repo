# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollpcm(RPackage):
	"""Collapsed Latent Position Cluster Model for Social Networks

	Markov chain Monte Carlo based inference routines for collapsed latent position cluster models or social networks, which includes searches over the model space (number of clusters in the latent position cluster model). The label switching algorithm used is that of Nobile and Fearnside (2007) <doi:10.1007/s11222-006-9014-7> which relies on the algorithm of Carpaneto and Toth (1980) <doi:10.1145/355873.355883>. 
	"""
	
	cran = "collpcm" 

	version("1.3", md5="22660bf4f71edfae7d5cdfaed0aea264")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-latentnet", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
