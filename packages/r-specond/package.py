# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecond(RPackage):
	"""Condition specific detection from expression data

	This package performs a gene expression data analysis to detect condition-specific genes. Such genes are significantly up- or down-regulated in a small number of conditions. It does so by fitting a mixture of normal distributions to the expression values. Conditions can be environmental conditions, different tissues, organs or any other sources that you wish to compare in terms of gene expression.
	"""
	
	bioc = "SpeCond" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SpeCond_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SpeCond/SpeCond_1.56.0.tar.gz"]

	version("1.56.0", sha256="18912073851a4e4f6d76982fbe06a3dac4a9332e50608f918d124fdb299678bc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mclust@3.3.1:", type=("build", "run"))
	depends_on("r-biobase@1.15.13:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-hwriter@1.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
