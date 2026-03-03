# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeclustnet(RPackage):
	"""Fit the Mixture of Experts Latent Position Cluster Model to
Network Data

	Functions to facilitate model-based clustering of nodes in a network in a mixture of experts setting, which incorporates covariate information on the nodes in the modelling process. Isobel Claire Gormley and Thomas Brendan Murphy (2010) <doi:10.1016/j.stamet.2010.01.002>.
	"""
	
	cran = "MEclustnet" 

	version("1.2.2", md5="8c2a2f54bf4e0e772d6b153d1fbe21e7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-latentnet", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
