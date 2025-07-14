# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeltagseg(RPackage):
	"""deltaGseg

	Identifying distinct subpopulations through multiscale time series analysis
	"""
	
	bioc = "deltaGseg" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/deltaGseg_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/deltaGseg/deltaGseg_1.42.0.tar.gz"]

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="ae5990a978668b59fd31849ef395fedca1c6b641a7acf22b51440253195a0217")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-pvclust", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
