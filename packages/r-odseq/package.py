# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdseq(RPackage):
	"""Outlier detection in multiple sequence alignments

	Performs outlier detection of sequences in a multiple sequence alignment using bootstrap of predefined distance metrics. Outlier sequences can make downstream analyses unreliable or make the alignments less accurate while they are being constructed. This package implements the OD-seq algorithm proposed by Jehl et al (doi 10.1186/s12859-015-0702-1) for aligned sequences and a variant using string kernels for unaligned sequences.
	"""
	
	bioc = "odseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/odseq_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/odseq/odseq_1.30.0.tar.gz"]

	version("1.30.0", sha256="2dae113510f5e0f5663d49da684dcb1c4dc0601489b0e1ab00918fa29300671e")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-msa@1.2.1:", type=("build", "run"))
	depends_on("r-kebabs@1.4.1:", type=("build", "run"))
	depends_on("r-mclust@5.1:", type=("build", "run"))
