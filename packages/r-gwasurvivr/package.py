# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasurvivr(RPackage):
	"""gwasurvivr: an R package for genome wide survival analysis

	gwasurvivr is a package to perform survival analysis using Cox proportional hazard models on imputed genetic data.
	"""
	
	homepage = "https://github.com/suchestoncampbelllab/gwasurvivr"
	bioc = "gwasurvivr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gwasurvivr_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gwasurvivr/gwasurvivr_1.20.0.tar.gz"]

	version("1.20.0", md5="699843eb7ff1528732a6a2e093600aef")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gwastools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-snprelate", type=("build", "run"))
