# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynextend(RPackage):
	"""Tools for Working With Synteny Objects

	Shared order between genomic sequences provide a great deal of information. Synteny objects produced by the R package DECIPHER provides quantitative information about that shared order. SynExtend provides tools for extracting information from Synteny objects.
	"""
	
	bioc = "SynExtend" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SynExtend_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SynExtend/SynExtend_1.14.0.tar.gz"]

	version("1.20.2", tag="RELEASE_3_21")
	version("1.14.0", sha256="f64c5a7398822d196098bbe576c76aec05e8bdaf5db925f7d701485cc528d1ef")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-decipher@2.28:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
