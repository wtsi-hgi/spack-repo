# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdshop(RPackage):
	"""High-Dimensional Shrinkage Optimal Portfolios

	Constructs shrinkage estimators of high-dimensional mean-variance portfolios and performs 
    high-dimensional tests on optimality of a given portfolio. The techniques developed in 
    Bodnar et al. (2018 <doi:10.1016/j.ejor.2017.09.028>, 2019 <doi:10.1109/TSP.2019.2929964>, 
    2020 <doi:10.1109/TSP.2020.3037369>, 2021 <doi:10.1080/07350015.2021.2004897>) 
    are central to the package. They provide simple and feasible estimators and tests for optimal 
    portfolio weights, which are applicable for 'large p and large n' situations where p is the 
    portfolio dimension (number of stocks) and n is the sample size. The package also includes tools
    for constructing portfolios based on shrinkage estimators of the mean vector and covariance matrix
    as well as a new Bayesian estimator for the Markowitz efficient frontier recently developed by 
    Bauder et al. (2021) <doi:10.1080/14697688.2020.1748214>.
	"""
	
	homepage = "https://github.com/Otryakhin-Dmitry/global-minimum-variance-portfolio"
	cran = "HDShOP" 

	version("0.1.5", md5="b7a0f274ab6bfe40b36eb5e135c8943e")
	version("0.1.3", md5="4aeab0cca2022a6a67445275a04dab71")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
