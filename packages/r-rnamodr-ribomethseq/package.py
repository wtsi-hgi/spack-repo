# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamodrRibomethseq(RPackage):
	"""Detection of 2'-O methylations by RiboMethSeq

	RNAmodR.RiboMethSeq implements the detection of 2'-O methylations on RNA from experimental data generated with the RiboMethSeq protocol. The package builds on the core functionality of the RNAmodR package to detect specific patterns of the modifications in high throughput sequencing data.
	"""
	
	homepage = "https://github.com/FelixErnst/RNAmodR.RiboMethSeq"
	bioc = "RNAmodR.RiboMethSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNAmodR.RiboMethSeq_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNAmodR.RiboMethSeq/RNAmodR.RiboMethSeq_1.16.0.tar.gz"]

	version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="e3a50ae6290f77cb090b696886382f7022e11ea77dab9e8a0431f591d29dcb64")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rnamodr@1.5.3:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
