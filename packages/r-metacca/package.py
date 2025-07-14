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

	version("1.36.0", commit="af2b37762a86b80c9a5b332c229406b8a41852bf")
	version("1.30.0", commit="c8e65857a8a41cb49f65353fd26b3861deb0d2da")

