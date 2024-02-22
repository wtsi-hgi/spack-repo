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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/deltaGseg_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/deltaGseg/deltaGseg_1.42.0.tar.gz"]

	version("1.42.0", md5="e92ca25a67a9250f26c6263043c60ee2")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-pvclust", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
