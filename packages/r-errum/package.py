# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErrum(RPackage):
	"""Exploratory Reduced Reparameterized Unified Model Estimation

	Perform a Bayesian estimation of the exploratory reduced
    reparameterized unified model (ErRUM) described by Culpepper and Chen (2018)
    <doi:10.3102/1076998618791306>.
	"""
	
	homepage = "https://github.com/tmsalab/errum"
	cran = "errum" 

	version("0.0.3", md5="8e884ce3d7bd7b30a259e4b2c34a9e9e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.200:", type=("build", "run"))
