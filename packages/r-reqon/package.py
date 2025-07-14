# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReqon(RPackage):
	"""Recalibrating Quality Of Nucleotides

	Algorithm for recalibrating the base quality scores for aligned sequencing data in BAM format.
	"""
	
	bioc = "ReQON"

	version("1.48.0", commit="9a9023213ccdeb6c70fd1d1d0b4ca968dda8a6ac")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-seqbias", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
