# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilterffpe(RPackage):
	"""FFPE Artificial Chimeric Read Filter for NGS data

	This package finds and filters artificial chimeric reads specifically generated in next-generation sequencing (NGS) process of formalin-fixed paraffin-embedded (FFPE) tissues. These artificial chimeric reads can lead to a large number of false positive structural variation (SV) calls. The required input is an indexed BAM file of a FFPE sample.
	"""
	
	bioc = "FilterFFPE"

	version("1.18.0", commit="fe0b6cd1aaca4e5571ce3d2f41f055f8b6fbac38")
	version("1.12.0", commit="d78f5187baee0e0e29bcda1fc43d005cbc3e26c6")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
