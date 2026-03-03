# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinspp(RPackage):
	"""Bayesian Inference for Neyman-Scott Point Processes

	The Bayesian MCMC estimation of parameters for Thomas-type cluster
    point process with various inhomogeneities. It allows for inhomogeneity in
    (i) distribution of parent points, (ii) mean number of points in a cluster,
    (iii) cluster spread. The package also allows for the Bayesian MCMC
    algorithm for the homogeneous generalized Thomas process. The cluster size
    is allowed to have a variance that is greater or less than the expected
    value (cluster sizes are over or under dispersed). Details are described in
    Dvořák, Remeš, Beránek & Mrkvička (2022) <arXiv: 10.48550/arXiv.2205.07946>.
	"""
	
	homepage = "https://github.com/tomasmrkvicka/binspp"
	cran = "binspp" 

	version("0.1.26", md5="8585c128a7443ba6a0097aef2d3e2c82")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-spatstat", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
