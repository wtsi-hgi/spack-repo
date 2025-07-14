# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnits(RPackage):
	"""R Normalization and Inference of Time Series data

	R/Bioconductor package for normalization, curve registration and inference in time course gene expression data.
	"""
	
	bioc = "Rnits" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rnits_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rnits/Rnits_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="97caa20725437fd6ea545de91967347c08a8459a4c07b3a87e49a0a34310b924")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
