# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqmagick(RPackage):
	"""Sequence Manipulation Utilities

	Supports reading and writing sequences for different formats (currently interleaved and sequential formats for 'FASTA' and 'PHYLIP'), file conversion, and manipulation (e.g. filter sequences that contain specify pattern, export consensus sequence from an alignment).
	"""
	
	homepage = "https://github.com/YuLab-SMU/seqmagick"
	cran = "seqmagick" 

	version("0.1.7", md5="e2923b561cb82289ef07e4016f7376ad")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-yulab-utils@0.1.1:", type=("build", "run"))
