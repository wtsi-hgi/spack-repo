# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiscan(RPackage):
	"""Scan Pairwise Epistasis

	Searching genomic interactions with linear/logistic regression in a high-dimensional dataset is a time-consuming task. This package provides some efficient ways to scan epistasis in genome-wide interaction studies (GWIS). Both case-control status (binary outcome) and quantitative phenotype (continuous outcome) are supported (the main references: 1. Kam-Thong, T., D. Czamara, K. Tsuda, K. Borgwardt, C. M. Lewis, A. Erhardt-Lehmann, B. Hemmer, et al. (2011). <doi:10.1038/ejhg.2010.196>. 2. Kam-Thong, T., B. Pütz, N. Karbalai, B. Müller-Myhsok, and K. Borgwardt. (2011).  <doi:10.1093/bioinformatics/btr218>.)
	"""
	
	cran = "episcan" 

	version("0.0.1", md5="0a912efcac4309d51c91efa1c7ade117")

	depends_on("r@3.5:", type=("build", "run"))
