# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioqc(RPackage):
	"""Detect tissue heterogeneity in expression profiles with gene sets

	BioQC performs quality control of high-throughput expression data based on tissue gene signatures. It can detect tissue heterogeneity in gene expression data. The core algorithm is a Wilcoxon-Mann-Whitney test that is optimised for high performance.
	"""
	
	homepage = "https://accio.github.io/BioQC"
	bioc = "BioQC"

	version("1.36.0", commit="2e46294e16a07d5eff00921608a969eaef0035eb")
	version("1.30.0", commit="e232c7781b9d035a19c9176cc1b9582263fe0032")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
