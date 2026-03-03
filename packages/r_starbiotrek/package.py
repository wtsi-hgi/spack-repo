# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarbiotrek(RPackage):
	"""StarBioTrek

	This tool StarBioTrek presents some methodologies to measure pathway activity and cross-talk among pathways integrating also the information of network data.
	"""
	
	homepage = "https://github.com/claudiacava/StarBioTrek"
	bioc = "StarBioTrek" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/StarBioTrek_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/StarBioTrek/StarBioTrek_1.28.0.tar.gz"]

	version("1.28.0", md5="a1a892a63f09a57e18eb825ab8a0ec7e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-spidermir", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
