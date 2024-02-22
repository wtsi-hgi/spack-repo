# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbglmnet(RPackage):
	"""Empirical Bayesian Lasso and Elastic Net Methods for Generalized
Linear Models

	Provides empirical Bayesian lasso and elastic net algorithms for variable selection and effect estimation. Key features include sparse variable selection and effect estimation via generalized linear regression models, high dimensionality with p>>n, and significance test for nonzero effects. This package outperforms other popular methods such as lasso and elastic net methods in terms of power of detection, false discovery rate, and power of detecting grouping effects. Please reference its use as A Huang and D Liu (2016) <doi: 10.1093/bioinformatics/btw143>.
	"""
	
	homepage = "https://sites.google.com/site/anhuihng/"
	cran = "EBglmnet" 

	version("6.0", md5="820833f1f9018fa6b0fe3f7a457d2de3")

	depends_on("r@2.10:", type=("build", "run"))
