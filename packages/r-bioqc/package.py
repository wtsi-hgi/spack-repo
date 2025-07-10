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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BioQC_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BioQC/BioQC_1.30.0.tar.gz"]

	version("1.30.0", sha256="8a4e7c5e2e5e245274a87c920909536d1652aec0cc9a35a81730152140787596")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
