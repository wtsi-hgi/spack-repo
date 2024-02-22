# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondmvt(RPackage):
	"""Conditional Multivariate t Distribution, Expectation
Maximization Algorithm, and Its Stochastic Variants

	Computes conditional multivariate t probabilities, random deviates, and densities. It can also be used to create missing values at random in a dataset, resulting in a missing at random (MAR) mechanism. Inbuilt in the package are the Expectation-Maximization (EM), Monte Carlo EM, and Stochastic EM algorithms for imputation of missing values in datasets assuming the multivariate t distribution. See Kinyanjui, Tamba, Orawo, and Okenye (2020)<doi:10.3233/mas-200493>, and Kinyanjui, Tamba, and Okenye(2021)<http://www.ceser.in/ceserp/index.php/ijamas/article/view/6726/0> for more details. 
	"""
	
	cran = "CondMVT" 

	version("0.1.0", md5="6982ec415413afb3125a03ce417b0053")

	depends_on("r-mvtnorm", type=("build", "run"))
