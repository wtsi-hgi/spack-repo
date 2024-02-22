# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtergm(RPackage):
	"""Temporal Exponential Random Graph Models by Bootstrapped
Pseudolikelihood

	Temporal Exponential Random Graph Models (TERGM) estimated by maximum pseudolikelihood with bootstrapped confidence intervals or Markov Chain Monte Carlo maximum likelihood. Goodness of fit assessment for ERGMs, TERGMs, and SAOMs. Micro-level interpretation of ERGMs and TERGMs. The methods are described in Leifeld, Cranmer and Desmarais (2018), JStatSoft <doi:10.18637/jss.v083.i06>.
	"""
	
	homepage = "https://github.com/leifeld/btergm"
	cran = "btergm" 

	version("1.10.11", md5="010e57b5f3a5642b3d57ec84a7271edc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-network@1.17.1:", type=("build", "run"))
	depends_on("r-sna@2.3.2:", type=("build", "run"))
	depends_on("r-ergm@4.2.1:", type=("build", "run"))
	depends_on("r-matrix@1.3.2:", type=("build", "run"))
	depends_on("r-boot@1.3.17:", type=("build", "run"))
	depends_on("r-coda@0.18.1:", type=("build", "run"))
	depends_on("r-rocr@1.0.7:", type=("build", "run"))
	depends_on("r-igraph@0.7.1:", type=("build", "run"))
	depends_on("r-statnet-common@4.5:", type=("build", "run"))
