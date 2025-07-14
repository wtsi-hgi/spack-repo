# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterRanges(RPackage):
	"""Load and Save Ranges-related Artifacts from File

	Save GenomicRanges, IRanges and related data structures into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.ranges"

	version("1.8.0", commit="62d3a4fc945f76548c9c8107c44f2a980f8abd01")
	version("1.2.0", commit="c7a063d3d93bafdda4994d67f80949e986ebc3ec")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
