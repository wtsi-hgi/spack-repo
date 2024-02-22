# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrcte(RPackage):
	"""Statistical Approaches for Time-to-Event Data in Agriculture

	A specific and comprehensive framework for the analyses of time-to-event data in agriculture. Fit non-parametric and parametric time-to-event models. Compare time-to-event curves for different experimental groups. Plots and other displays. It is particularly tailored to the analyses of data from germination and emergence assays. The methods are described in Onofri et al. (2020) "A unified framework for the analysis of germination, emergence, and other time-to-event data in weed science"", Weed Science, 70, 259-271 <doi:10.1017/wsc.2022.8>.
	"""
	
	homepage = "https://www.statforbiology.com"
	cran = "drcte" 

	version("1.0.30", md5="7f80916cbbf427156a0f683b63a5744b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
