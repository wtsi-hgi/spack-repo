# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwalign(RPackage):
	"""Perform pairwise sequence alignments.

	The package provides pairwiseAlignment() and stringDist() helpers to run
	global, local, and overlap alignments, plus utilities to summarize and
	score those results."""

	bioc = "pwalign"

	version("1.6.0", tag="RELEASE_3_22")
	version("1.4.0", tag="RELEASE_3_21")
	version("1.2.0", tag="RELEASE_3_20")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings@2.71.5:", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
