# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBader(RPackage):
	"""Bayesian Analysis of Differential Expression in RNA Sequencing Data

	For RNA sequencing count data, BADER fits a Bayesian hierarchical model. The algorithm returns the posterior probability of differential expression for each gene between two groups A and B. The joint posterior distribution of the variables in the model can be returned in the form of posterior samples, which can be used for further down-stream analyses such as gene set enrichment.
	"""
	
	bioc = "BADER" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BADER_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BADER/BADER_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="d597dfa44e9c0dffc8bae73cced5b21bfeea76fb7523f2d84bd36a4e8f3aae7e")

