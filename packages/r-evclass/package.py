# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvclass(RPackage):
	"""Evidential Distance-Based Classification

	Different evidential classifiers, which provide
    outputs in the form of Dempster-Shafer mass functions. The methods are: 
    the evidential K-nearest neighbor rule, the evidential neural 
    network, radial basis function neural networks, logistic regression,
    feed-forward neural networks.
	"""
	
	cran = "evclass" 

	version("2.0.2", md5="3d268b37d97e8bef4ac0614ad9aaefee")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ibelief", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
