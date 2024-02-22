# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSentometrics(RPackage):
	"""An Integrated Framework for Textual Sentiment Time Series
Aggregation and Prediction

	Optimized prediction based on textual sentiment, accounting for the intrinsic challenge that sentiment can be computed and pooled across texts and time in various ways. See Ardia et al. (2021) <doi:10.18637/jss.v099.i02>.
	"""
	
	homepage = "https://sentometrics-research.com/sentometrics/"
	cran = "sentometrics" 

	version("1.0.0", md5="80e2f957a80625f71b65efc87fff89aa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-isoweek", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
