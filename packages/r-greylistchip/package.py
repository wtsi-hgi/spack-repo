# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreylistchip(RPackage):
	"""Grey Lists -- Mask Artefact Regions Based on ChIP Inputs

	Identify regions of ChIP experiments with high signal in the input, that lead to spurious peaks during peak calling. Remove reads aligning to these regions prior to peak calling, for cleaner ChIP analysis.
	"""
	
	bioc = "GreyListChIP"

	version("1.40.0", commit="9700ac4c5ff2c8eb751105e4fb7ce35e968fdfba")
	version("1.34.0", commit="75f5a62e750daa9565d72cc26ea20c76545adeb6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
