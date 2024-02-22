# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeach(RPackage):
	"""Pareto Enrichment Analysis for Combining Heterogeneous Datasets

	A meta gene set analysis tool developed based on principles of Pareto dominance (William B T Mock (2011) <doi:10.1007/978-1-4020-9160-5_341>). It is designed to combine gene set analysis p-values from multiple transcriptome datasets (e.g., microarray and RNA-Seq). The novel Pareto method for p-value combination allows PEACH to properly model heterogeneity and correlation in Omics datasets.
	"""
	
	cran = "PEACH" 

	version("0.1.1", md5="6fa73d15215eb6fbc7e02c7c7b9732e6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass@7.3.50:", type=("build", "run"))
	depends_on("r-mnormt@1.5.6:", type=("build", "run"))
	depends_on("r-metap@1.3:", type=("build", "run"))
