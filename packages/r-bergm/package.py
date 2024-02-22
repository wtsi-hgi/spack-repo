# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBergm(RPackage):
	"""Bayesian Exponential Random Graph Models

	Bayesian analysis for exponential random graph models using
    advanced computational algorithms. More information can be found at:
    <https://acaimo.github.io/Bergm/>.
	"""
	
	homepage = "https://acaimo.github.io/Bergm/"
	cran = "Bergm" 

	version("5.0.7", md5="5c72aacf9a396fab6611733ce10409ca")

	depends_on("r-ergm", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
