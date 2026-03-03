# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsem(RPackage):
	"""Robust Structural Equation Modeling with Missing Data and
Auxiliary Variables

	A robust procedure is implemented to estimate means and covariance matrix of multiple variables with missing data using Huber weight and then to estimate a structural equation model.
	"""
	
	homepage = "https://bigdatalab.nd.edu"
	cran = "rsem" 

	version("0.5.1", md5="3beb080d8e6d68b35abebd5c597cd393")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
