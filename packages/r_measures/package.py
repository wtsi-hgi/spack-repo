# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeasures(RPackage):
	"""Performance Measures for Statistical Learning

	Provides the biggest amount of statistical measures in the whole R world. Includes measures of regression, (multiclass) classification and multilabel classification. The measures come mainly from the 'mlr' package and were programed by several 'mlr' developers. 
	"""
	
	cran = "measures" 

	version("0.3", md5="470541e95f5000aa00a77a9904ef327f")

	depends_on("r@3:", type=("build", "run"))
