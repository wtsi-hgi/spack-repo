# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinarybalancedcut(RPackage):
	"""Threshold Cut Point of Probability for a Binary Classifier Model

	Allows to view the optimal probability cut-off point at which the Sensitivity and Specificity meets and its a best way to minimize both Type-1 and Type-2 error for a binary Classifier in determining the Probability threshold.
	"""
	
	cran = "BinarybalancedCut" 

	version("0.2", md5="9410765bba8155b46ef9e00e73187ad4")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
