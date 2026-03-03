# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGigg(RPackage):
	"""Group Inverse-Gamma Gamma Shrinkage for Sparse Regression with
Grouping Structure

	A Gibbs sampler corresponding to a Group 
    Inverse-Gamma Gamma (GIGG) regression model with adjustment covariates. 
    Hyperparameters in the GIGG prior specification can either be fixed by the 
    user or can be estimated via Marginal Maximum Likelihood Estimation.
    Jonathan Boss, Jyotishka Datta, Xin Wang, Sung Kyun Park, Jian Kang, Bhramar 
    Mukherjee (2021) <arXiv:2102.10670>.
	"""
	
	homepage = "https://github.com/umich-cphds/gigg"
	cran = "gigg" 

	version("0.2.1", md5="fdafcc7c3dd1955e69484172bf06e851")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
