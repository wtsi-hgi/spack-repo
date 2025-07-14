# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicalignments(RPackage):
	"""Representation and manipulation of short genomic alignments.

	Provides efficient containers for storing and manipulating short genomic
	alignments (typically obtained by aligning short reads to a reference
	genome). This includes read counting, computing the coverage, junction
	detection, and working with the nucleotide content of the alignments."""

	bioc = "GenomicAlignments"
	version("1.44.0", commit="41db306111154fd8249d1d785d48b76cc62047d9")
	version("1.38.2", commit="d740c47c93acb6892aeb8dda8f29091bf793bb35")
	version("1.36.0", commit="cdc1aa49f14d3effe2540380a04fe1fc72c00f04")
	version("1.34.0", commit="c6eb78079c8aa21d47c95b3d16a606e8c2c5d799")
	version("1.32.1", commit="2553580d0b8a8a5fd7835c1446616b39f707b8a9")
	version("1.32.0", commit="7a660a914a04e2eb0758082b6f64c4124a887ef3")
	version("1.30.0", commit="2d2c5fce3529c2962fdcefd736d8b7f7c0ec2d54")
	version("1.26.0", commit="6c74c74ee53efcd880171126366fee4bd72357bc")
	version("1.20.1", commit="9dce402071e4cd945de7ff82ea574c79993625fd")
	version("1.18.1", commit="8ac41e5981cf343076044f451a984afb651688ab")
	version("1.16.0", commit="db032a459e5cf05a2a5c2059662a541827112974")
	version("1.14.2", commit="57b0b35d8b36069d4d94af86af051f0129b28eef")
	version("1.12.2", commit="b5d6f19e4a89b6c1c3e9e58e5ea4eb13870874ef")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb@1.13.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.9.13:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
