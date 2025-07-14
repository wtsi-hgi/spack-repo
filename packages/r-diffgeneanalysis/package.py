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

	version("1.90.0", commit="3b65b8b1edd695e92b522a9fafc8863ad3d026c8")
	version("1.84.0", commit="0f01211b49fa5f15c6f3442af76d0a44b5ef2100")

	depends_on("r-minpack-lm@1.0.4:", type=("build", "run"))
