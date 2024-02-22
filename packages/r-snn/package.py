# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnn(RPackage):
	"""Stabilized Nearest Neighbor Classifier

	Implement K-nearest neighbor classifier, weighted nearest neighbor classifier, bagged nearest neighbor classifier, optimal weighted nearest neighbor classifier and stabilized nearest neighbor classifier, and perform model selection via 5 fold cross-validation for them. This package also provides functions for computing the classification error and classification instability of a classification procedure.
	"""
	
	cran = "snn" 

	version("1.1", md5="dd815b61c131fe2f264b6448de0c28e1")

	depends_on("r@3:", type=("build", "run"))
