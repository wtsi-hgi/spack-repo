# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmbc(RPackage):
	"""Robust Model Based Clustering

	A robust clustering algorithm (Model-Based) similar to Expectation
    Maximization for finite mixture normal distributions is implemented, 
    its main advantage is that the estimator is resistant to outliers, 
    that means that results of parameter estimation are still correct when there
    are atypical values in the sample 
    (see Gonzalez, Maronna, Yohai and Zamar (2021) 
    <arxiv:2102.06851>). 
	"""
	
	cran = "RMBC" 

	version("0.1.0", md5="caa60381d99624b92e66634c5407239c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ktaucenters", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
