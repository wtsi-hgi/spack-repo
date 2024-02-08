# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProc(RPackage):
	"""Display and Analyze ROC Curves.

	Tools for visualizing, smoothing and comparing receiver operating
	characteristic (ROC curves). (Partial) area under the curve (AUC) can be
	compared with statistical tests based on U-statistics or bootstrap.
	Confidence intervals can be computed for (p)AUC or ROC curves."""

	cran = "pROC"

	version("1.18.5", md5="61d0e89dd7b4cb5e506cdfb6fc28848a")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
