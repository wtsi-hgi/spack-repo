# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiger(RPackage):
	"""Lightweight Iterative Geneset Enrichment

	Gene Set Enrichment Analysis (GSEA) is a computational method that determines whether an a priori defined set of genes shows statistically significant, concordant differences between two biological states. The original algorithm is detailed in Subramanian et al. with 'Java' implementations available through the Broad Institute (Subramanian et al. 2005 <doi:10.1073/pnas.0506580102>). The 'liger' package provides a lightweight R implementation of this enrichment test on a list of values (Fan et al., 2017 <doi:10.5281/zenodo.887386>). Given a list of values, such as p-values or log-fold changes derived from differential expression analysis or other analyses comparing biological states, this package enables you to test a priori defined set of genes for enrichment to enable interpretability of highly significant or high fold-change genes.
	"""
	
	homepage = "https://github.com/JEFworks/liger"
	cran = "liger" 

	version("2.0.1", md5="d7a410589d361d183968613aeed4fd2a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
