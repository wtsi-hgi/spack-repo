# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLam(RPackage):
	"""Some Latent Variable Models

	
    Includes some procedures for latent variable modeling with a 
    particular focus on multilevel data.
    The 'LAM' package contains mean and covariance structure modelling
    for multivariate normally distributed data (mlnormal(); Longford, 1987;
    <doi:10.1093/biomet/74.4.817>), a general Metropolis-Hastings algorithm 
    (amh(); Roberts & Rosenthal, 2001, <doi:10.1214/ss/1015346320>) and 
    penalized maximum likelihood estimation (pmle(); Cole, Chu & Greenland, 
    2014; <doi:10.1093/aje/kwt245>).
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/LAM"
	cran = "LAM" 

	version("0.6-19", md5="56a6fd9c496d2d147d3671160c8ecf77")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cdm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sirt", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
