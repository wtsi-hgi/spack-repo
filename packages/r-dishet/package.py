# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDishet(RPackage):
	"""Estimate the Gene Expression Levels and Component Proportions of
the Normal, Stroma (Immune) and Tumor Components of Bulk Tumor
Samples

	Model cell type heterogeneity of bulk renal cell carcinoma. The observed gene expression in bulk tumor sample is modeled by a log-normal distribution with the location parameter structured as a linear combination of the component-specific gene expressions. 
	"""
	
	cran = "DisHet" 

	version("1.0.0", md5="dddad7c9a0ee40e86784e407b500566d")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
