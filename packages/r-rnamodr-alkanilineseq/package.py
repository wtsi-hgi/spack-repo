# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamodrAlkanilineseq(RPackage):
	"""Detection of m7G, m3C and D modification by AlkAnilineSeq

	RNAmodR.AlkAnilineSeq implements the detection of m7G, m3C and D modifications on RNA from experimental data generated with the AlkAnilineSeq protocol. The package builds on the core functionality of the RNAmodR package to detect specific patterns of the modifications in high throughput sequencing data.
	"""
	
	homepage = "https://github.com/FelixErnst/RNAmodR.AlkAnilineSeq"
	bioc = "RNAmodR.AlkAnilineSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNAmodR.AlkAnilineSeq_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNAmodR.AlkAnilineSeq/RNAmodR.AlkAnilineSeq_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="b5b5a629768692428cc3e6bf68e7427c100707924373e14ca672717a2a02cfe0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rnamodr@1.5.3:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
