# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylsig(RPackage):
	"""MethylSig: Differential Methylation Testing for WGBS and RRBS Data

	MethylSig is a package for testing for differentially methylated cytosines (DMCs) or regions (DMRs) in whole-genome bisulfite sequencing (WGBS) or reduced representation bisulfite sequencing (RRBS) experiments.  MethylSig uses a beta binomial model to test for significant differences between groups of samples. Several options exist for either site-specific or sliding window tests, and variance estimation.
	"""
	
	bioc = "methylSig" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/methylSig_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/methylSig/methylSig_1.14.0.tar.gz"]

	version("1.14.0", sha256="6c058ea0bc432db802feef72a22a26f8ab970e2f27b695f30e39c5c3ca7617ed")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-dss", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
