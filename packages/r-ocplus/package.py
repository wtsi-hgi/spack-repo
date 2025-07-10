# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcplus(RPackage):
	"""Operating characteristics plus sample size and local fdr for microarray experiments

	This package allows to characterize the operating characteristics of a microarray experiment, i.e. the trade-off between false discovery rate and the power to detect truly regulated genes. The package includes tools both for planned experiments (for sample size assessment) and for already collected data (identification of differentially expressed genes).
	"""
	
	bioc = "OCplus" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OCplus_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OCplus/OCplus_1.76.0.tar.gz"]

	version("1.76.0", sha256="372345e32f524a9dd287016acdb0e9385ce62e4c6e0045620f0a76c417c3ec9a")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-multtest@1.7.3:", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
