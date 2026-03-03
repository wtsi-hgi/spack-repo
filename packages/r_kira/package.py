# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKira(RPackage):
	"""Machine Learning

	Machine learning, containing several algorithms for supervised and unsupervised classification, in addition to a function that plots the Receiver Operating Characteristic (ROC) and Precision-Recall (PRC) curve graphs, and also a function that returns several metrics used for model evaluation, the latter can be used in ranking results from other packs.
	"""
	
	cran = "Kira" 

	version("1.0.1", md5="12e635c46ca0f6990cff36b001a5ac01")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
