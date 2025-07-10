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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GreyListChIP_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GreyListChIP/GreyListChIP_1.34.0.tar.gz"]

	version("1.34.0", sha256="d945de29328d081f2354ceb892d918ee8abd06418a8a79ac7388cee5362327cd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
