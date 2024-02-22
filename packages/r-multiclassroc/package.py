# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticlassroc(RPackage):
	"""ROC Curves for Multi-Class Analysis

	Function multiroc() can be used for computing and visualizing Receiver Operating Characteristics (ROC) and Area Under the Curve (AUC) for multi-class classification problems. It supports both One-vs-One approach by M.Bishop, C. (2006, ISBN:978-0-387-31073-2) and One-vs-All approach by Murphy P., K. (2012, ISBN:9780262018029).
	"""
	
	cran = "MultiClassROC" 

	version("0.1.0", md5="1c650d9f9c8e641235d4964394b6c3de")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
