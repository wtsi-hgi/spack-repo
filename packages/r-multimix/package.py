# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimix(RPackage):
	"""Fit Mixture Models Using the Expectation Maximisation (EM)
Algorithm

	A set of functions which use the Expectation Maximisation (EM) 
    algorithm (Dempster, A. P., Laird, N. M., and Rubin, D. B. (1977) 
    <doi:10.1111/j.2517-6161.1977.tb01600.x> Maximum likelihood from 
    incomplete data via the EM algorithm, Journal of the Royal Statistical 
    Society, 39(1), 1--22) to take a finite mixture model approach to 
    clustering. The package is designed to cluster multivariate data that have 
    categorical and continuous variables and that possibly contain missing 
    values. The method is described in Hunt, L. and Jorgensen, M. (1999) 
    <doi:10.1111/1467-842X.00071> Australian & New Zealand Journal of Statistics 
    41(2), 153--171 and Hunt, L. and Jorgensen, M. (2003) 
    <doi:10.1016/S0167-9473(02)00190-1> Mixture model clustering for mixed data 
    with missing information, Computational Statistics & Data Analysis, 41(3-4), 
    429--440.
	"""
	
	homepage = "https://github.com/jmcurran/multimix"
	cran = "multimix" 

	version("1.0-10", md5="db4d761814aac8bf0ff550e44967b548")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
