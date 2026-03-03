# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutforest(RPackage):
	"""Multivariate Outlier Detection and Replacement

	Provides a random forest based implementation of the method
    described in Chapter 7.1.2 (Regression model based anomaly detection)
    of Chandola et al. (2009) <doi:10.1145/1541880.1541882>. It works as
    follows: Each numeric variable is regressed onto all other variables
    by a random forest. If the scaled absolute difference between observed
    value and out-of-bag prediction of the corresponding random forest is
    suspiciously large, then a value is considered an outlier. The package
    offers different options to replace such outliers, e.g. by realistic
    values found via predictive mean matching. Once the method is trained
    on a reference data, it can be applied to new data.
	"""
	
	homepage = "https://github.com/mayer79/outForest"
	cran = "outForest" 

	version("1.0.1", md5="a4542c9e692319707e6b4a5894452f9c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-missranger@2.1:", type=("build", "run"))
