# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffgeneanalysis(RPackage):
	"""Performs differential gene expression Analysis

	Analyze microarray data
	"""
	
	bioc = "diffGeneAnalysis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/diffGeneAnalysis_1.84.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/diffGeneAnalysis/diffGeneAnalysis_1.84.0.tar.gz"]

	version("1.90.0", tag="RELEASE_3_21")
	version("1.84.0", sha256="6021d33ab50d0682484571238dc5c1672462deef44e6259102bcf68b54d14d9d")

	depends_on("r-minpack-lm@1.0.4:", type=("build", "run"))
