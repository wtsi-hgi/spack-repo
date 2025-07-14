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

	version("1.52.0", commit="aa841a2ffe7d4edbdc1415e94a029277a900b99a")
	version("1.46.0", commit="7e3356dd8ad1211020b8593332c3119b4da69621")

	depends_on("r@2.14.1:", type=("build", "run"))
