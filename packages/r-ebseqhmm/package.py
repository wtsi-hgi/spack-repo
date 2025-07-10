# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbseqhmm(RPackage):
	"""Bayesian analysis for identifying gene or isoform expression changes in ordered RNA-seq experiments

	The EBSeqHMM package implements an auto-regressive hidden Markov model for statistical analysis in ordered RNA-seq experiments (e.g. time course or spatial course data). The EBSeqHMM package provides functions to identify genes and isoforms that have non-constant expression profile over the time points/positions, and cluster them into expression paths.
	"""
	
	bioc = "EBSeqHMM" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EBSeqHMM_1.35.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EBSeqHMM/EBSeqHMM_1.35.0.tar.gz"]

	version("1.35.0", sha256="b669e8154b1fb5e7f873c87d53009302148461ae08b586e33158b1048d6af7ed")

	depends_on("r-ebseq", type=("build", "run"))
