# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffcorr(RPackage):
	"""Analyzing and Visualizing Differential Correlation Networks in
Biological Data

	A method for identifying pattern changes between 2 experimental
         conditions in correlation networks (e.g., gene co-expression networks),
         which builds on a commonly used association measure, such as Pearson's
         correlation coefficient. This package includes functions to calculate
         correlation matrices for high-dimensional dataset and to test
         differential correlation, which means the changes in the correlation
         relationship among variables (e.g., genes and metabolites) between 2
         experimental conditions. 
	"""
	
	cran = "DiffCorr" 

	version("0.4.3", md5="7459e0540e8f1173d0f463864d7f66e9")

	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
