# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoar(RPackage):
	"""Identify differential APA usage from RNA-seq alignments

	Identify preferential usage of APA sites, comparing two biological conditions, starting from known alternative sites and alignments obtained from standard RNA-seq experiments.
	"""
	
	homepage = "https://github.com/vodkatad/roar/"
	bioc = "roar"

	version("1.44.1", commit="d2ea95a130a9ddca7b902c2ff5ead27b4cc5f5a0")
	version("1.38.0", commit="f1f9d9cc93c59eb5df5c18aa91276ba08eb216ad")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicalignments@0.99.4:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
