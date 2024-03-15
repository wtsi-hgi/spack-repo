# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlagme(RPackage):
	"""Analysis of Metabolomics GC/MS Data

	Fragment-level analysis of gas chromatography-massspectrometry metabolomics data.
	"""
	
	bioc = "flagme" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flagme_1.58.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flagme/flagme_1.58.0.tar.gz"]

	version("1.58.0", md5="ada68435478c0172b282919125008b1f")

	depends_on("r-gcspikelite", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-camera", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
