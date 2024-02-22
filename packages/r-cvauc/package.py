# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvauc(RPackage):
	"""Cross-Validated Area Under the ROC Curve Confidence Intervals

	Tools for working with and evaluating cross-validated area under the ROC curve (AUC) estimators.  The primary functions of the package are ci.cvAUC and ci.pooled.cvAUC, which report cross-validated AUC and compute confidence intervals for cross-validated AUC estimates based on influence curves for i.i.d. and pooled repeated measures data, respectively.  One benefit to using influence curve based confidence intervals is that they require much less computation time than bootstrapping methods.  The utility functions, AUC and cvAUC, are simple wrappers for functions from the ROCR package.
	"""
	
	homepage = "https://github.com/ledell/cvAUC"
	cran = "cvAUC" 

	version("1.1.4", md5="51a4fd138bd086bf49ee0c230a7fc4d9")

	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
