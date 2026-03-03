# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrzero(RPackage):
	"""Diet Mendelian Randomization

	Encodes several methods for performing Mendelian randomization analyses with summarized data. Similar to the 'MendelianRandomization' package, but with fewer bells and whistles, and less frequent updates. As described in Yavorska (2017) <doi:10.1093/ije/dyx034> and Broadbent (2020) <doi:10.12688/wellcomeopenres.16374.2>.
	"""
	
	cran = "MRZero" 

	version("0.1.0", md5="d4e58fea601a4307633e742596daa5b3")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-plotly@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-robustbase@0.92.6:", type=("build", "run"))
	depends_on("r-quantreg@5.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
