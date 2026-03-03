# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmmixssl(RPackage):
	"""Semi-Supervised Gaussian Mixture Model with a Missing-Data
Mechanism

	The algorithm of semi-supervised learning based on finite Gaussian mixture models with a missing-data mechanism is designed for a fitting g-class Gaussian mixture model via maximum likelihood (ML). It is proposed to treat the labels of the unclassified features as missing-data and to introduce a framework for their missing as in the pioneering work of Rubin (1976) for missing in incomplete data analysis. This dependency in the missingness pattern can be leveraged to provide additional information about the optimal classifier as specified by Bayes’ rule. 
	"""
	
	cran = "EMMIXSSL" 

	version("1.1.1", md5="aeafe8ba876f5f0a95c92c8c0af5799d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
