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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/diffGeneAnalysis_1.84.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/diffGeneAnalysis/diffGeneAnalysis_1.84.0.tar.gz"]

	version("1.84.0", md5="aa3d8c4ce3b83b8a6f02e87384dd649f")

	depends_on("r-minpack-lm@1.0.4:", type=("build", "run"))
