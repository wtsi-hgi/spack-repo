# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCma(RPackage):
	"""Synthesis of microarray-based classification

	This package provides a comprehensive collection of various microarray-based classification algorithms both from Machine Learning and Statistics. Variable Selection, Hyperparameter tuning, Evaluation and Comparison can be performed combined or stepwise in a user-friendly environment.
	"""
	
	bioc = "CMA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CMA_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CMA/CMA_1.60.0.tar.gz"]

	version("1.60.0", md5="6654a3ef8f06edc618b81b8a059b2139")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
