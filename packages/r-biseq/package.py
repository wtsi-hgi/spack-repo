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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiSeq_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiSeq/BiSeq_1.42.0.tar.gz"]

    version("1.48.1", tag="RELEASE_3_21")
	version("1.42.0", sha256="4faab2f1afc2d6852bb814e3533c429e9a91b55d8b920bce8ccc8c6ed7385d2a")

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
