# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetacca(RPackage):
	"""Summary Statistics-Based Multivariate Meta-Analysis of Genome-Wide Association Studies Using Canonical Correlation Analysis

	metaCCA performs multivariate analysis of a single or multiple GWAS based on univariate regression coefficients. It allows multivariate representation of both phenotype and genotype. metaCCA extends the statistical technique of canonical correlation analysis to the setting where original individual-level records are not available, and employs a covariance shrinkage algorithm to achieve robustness.
	"""
	
	homepage = "https://doi.org/10.1093/bioinformatics/btw052"
	bioc = "metaCCA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/metaCCA_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/metaCCA/metaCCA_1.30.0.tar.gz"]

	version("1.30.0", md5="d5be58f253912b275964a681a508234d")

