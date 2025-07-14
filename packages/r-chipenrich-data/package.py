# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipenrichData(RPackage):
	"""Companion package to chipenrich

	Supporting data for the chipenrich package. Includes pre-defined gene sets, gene locus definitions, and mappability estimates.
	"""
	
	bioc = "chipenrich.data"

	version("2.32.0", commit="17e3e4acc5c5133e37f0dd6e499de3e380e58ed2")
	version("2.26.0", commit="18414bb55b4009f92ff01824e3884a77d80925bd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

