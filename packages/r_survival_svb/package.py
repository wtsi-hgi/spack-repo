# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalSvb(RPackage):
	"""Fit High-Dimensional Proportional Hazards Models

	Implementation of methodology designed to perform: (i) variable 
    selection, (ii) effect estimation, and (iii) uncertainty quantification, 
    for high-dimensional survival data. Our method uses a spike-and-slab prior 
    with Laplace slab and Dirac spike and approximates the corresponding 
    posterior using variational inference, a popular method in machine learning 
    for scalable conditional inference. Although approximate, the variational 
    posterior provides excellent point estimates and good control of the false 
    discovery rate. For more information see Komodromos et al. (2021) 
    <arXiv:2112.10270>.
	"""
	
	homepage = "https://github.com/mkomod/survival.svb"
	cran = "survival.svb" 

	version("0.0-2", md5="86e76e36d6c205fd3b2e398f985a87ac")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
