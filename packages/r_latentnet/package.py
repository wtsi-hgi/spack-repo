# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatentnet(RPackage):
	"""Latent Position and Cluster Models for Statistical Networks

	Fit and simulate latent position and cluster models for statistical networks. See Krivitsky and Handcock (2008) <doi:10.18637/jss.v024.i05> and Krivitsky, Handcock, Raftery, and Hoff (2009) <doi:10.1016/j.socnet.2009.04.001>.
	"""
	
	homepage = "https://statnet.org"
	cran = "latentnet" 

	version("2.11.0", md5="415b7efd38822d1b2de1127283bd047f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ergm@4.2:", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-coda@0.17.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-statnet-common@4.1:", type=("build", "run"))
