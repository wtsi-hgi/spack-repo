# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaga(RPackage):
	"""GaGa hierarchical model for high-throughput data analysis

	Implements the GaGa model for high-throughput data analysis, including differential expression analysis, supervised gene clustering and classification. Additionally, it performs sequential sample size calculations using the GaGa and LNNGV models (the latter from EBarrays package).
	"""
	
	bioc = "gaga" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gaga_2.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gaga/gaga_2.48.0.tar.gz"]

	version("2.48.0", md5="d1b404912b9a23365c9085dc91e20a10")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ebarrays", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
