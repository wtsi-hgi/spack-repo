# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR3cseq(RPackage):
	"""Analysis of Chromosome Conformation Capture and Next-generation Sequencing (3C-seq)

	This package is used for the analysis of long-range chromatin interactions from 3C-seq assay.
	"""
	
	homepage = "http://r3cseq.genereg.net"
	bioc = "r3Cseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/r3Cseq_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/r3Cseq/r3Cseq_1.48.0.tar.gz"]

    version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="c8081fc10e77cdf73b0f3ca6f5a376bd1b2beebb550e70c6490cc0113c7393d2")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
