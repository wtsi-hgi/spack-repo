# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVblpcm(RPackage):
	"""Variational Bayes Latent Position Cluster Model for Networks

	Fit and simulate latent position and cluster models for network data, using a fast Variational Bayes approximation developed in Salter-Townshend and Murphy (2013) <doi:10.1016/j.csda.2012.08.004>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "VBLPCM" 

	version("2.4.9", md5="a9f2ead5eaa7dc5284aadc66fc020a8e")

	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
