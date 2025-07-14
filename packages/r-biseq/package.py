# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiseq(RPackage):
	"""Processing and analyzing bisulfite sequencing data

	The BiSeq package provides useful classes and functions to handle and analyze targeted bisulfite sequencing (BS) data such as reduced-representation bisulfite sequencing (RRBS) data. In particular, it implements an algorithm to detect differentially methylated regions (DMRs). The package takes already aligned BS data from one or multiple samples.
	"""
	
	bioc = "BiSeq"

	version("1.48.1", commit="840407efdb7249a98e4de32a9c75647cf6899db3")
	version("1.42.0", commit="7dce55a0d2ac6349b5f03b57f37832443393180e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-lokern", type=("build", "run"))
	depends_on("r-globaltest", type=("build", "run"))
