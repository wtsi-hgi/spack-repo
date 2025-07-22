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

	version("1.58.0", sha256="4818fe34e1b9edc1cacffbccb34ba3cff7c3f633e3a852cc9504ec7c136d38be")

	depends_on("r-gcspikelite", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-camera", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
