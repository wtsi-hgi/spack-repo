# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGapclosing(RPackage):
	"""Estimate Gaps Under an Intervention

	Provides functions to estimate the disparities across categories (e.g. Black and white) that persists if a treatment variable (e.g. college) is equalized. Makes estimates by treatment modeling, outcome modeling, and doubly-robust augmented inverse probability weighting estimation, with standard errors calculated by a nonparametric bootstrap. Cross-fitting is supported. Survey weights are supported for point estimation but not for standard error estimation; those applying this package with complex survey samples should consult the data distributor to select an appropriate approach for standard error construction, which may involve calling the functions repeatedly for many sets of replicate weights provided by the data distributor. The methods in this package are described in Lundberg (2021) <doi:10.31235/osf.io/gx4y3>.
	"""
	
	homepage = "https://ilundberg.github.io/gapclosing/"
	cran = "gapclosing" 

	version("1.0.2", md5="fbe005940a9305933aa154aa44da837f")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
