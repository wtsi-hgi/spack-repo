# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgseas(RPackage):
	"""'stats' for Seasonal Adjustment on the Fly with 'ggplot2'

	Provides 'ggplot2' 'stats' that estimate seasonally adjusted series 
    and rolling summaries such as rolling average on the fly for time series.
	"""
	
	cran = "ggseas" 

	version("0.5.4", md5="ad913e33909525f424d881de2e0d85a9")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-seasonal", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
