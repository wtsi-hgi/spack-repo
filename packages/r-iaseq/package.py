# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIaseq(RPackage):
	"""iASeq: integrating multiple sequencing datasets for detecting allele-specific events

	It fits correlation motif model to multiple RNAseq or ChIPseq studies to improve detection of allele-specific events and describe correlation patterns across studies.
	"""
	
	bioc = "iASeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iASeq_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iASeq/iASeq_1.46.0.tar.gz"]

	version("1.46.0", sha256="35f0563d9c1573290e1e726ff16099c580239e11c13577a39632e59634c29478")

	depends_on("r@2.14.1:", type=("build", "run"))
