# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqcat(RPackage):
	"""High Throughput Sequencing Cell Authentication Toolkit

	The seqCAT package uses variant calling data (in the form of VCF files) from high throughput sequencing technologies to authenticate and validate the source, function and characteristics of biological samples used in scientific endeavours.
	"""
	
	bioc = "seqCAT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/seqCAT_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/seqCAT/seqCAT_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="88e0bedc957df1778d5a47834124f7df6485238059214a17f75103eb4f5f78ca")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-genomicranges@1.26.4:", type=("build", "run"))
	depends_on("r-variantannotation@1.20.3:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.13.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-iranges@2.8.2:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales@0.4.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.12.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.4:", type=("build", "run"))
	depends_on("r-tidyr@0.6.1:", type=("build", "run"))
