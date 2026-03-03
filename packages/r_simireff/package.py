# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimireff(RPackage):
	"""Stochastic Simulation for Information Retrieval Evaluation:
Effectiveness Scores

	Provides tools for the stochastic simulation of effectiveness scores to mitigate
  data-related limitations of Information Retrieval evaluation research, as described in Urbano and
  Nagler (2018) <doi:10.1145/3209978.3210043>. These tools include: fitting, selection and plotting
  distributions to model system effectiveness, transformation towards a prespecified expected value,
  proxy to fitting of copula models based on these distributions, and simulation of new evaluation
  data from these distributions and copula models.
	"""
	
	homepage = "https://github.com/julian-urbano/simIReff/"
	cran = "simIReff" 

	version("1.0", md5="c434683d243f0d438b7a0aeed7e8db1e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rvinecopulib@0.2.8.1:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-bde", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
