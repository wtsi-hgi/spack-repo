# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonnest2(RPackage):
	"""Tests of Non-Nested Models.

	Testing non-nested models via theory supplied by Vuong (1989)
	<doi:10.2307/1912557>. Includes tests of model distinguishability and of
	model fit that can be applied to both nested and non-nested models. Also
	includes functionality to obtain confidence intervals associated with AIC
	and BIC. This material is partially based on work supported by the National
	Science Foundation under Grant Number SES-1061334."""

	cran = "nonnest2"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("0.5-6", md5="404b9edab7bb21841bd359fdfc2c5c82", url="https://cran.r-project.org/src/contrib/nonnest2_0.5-6.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lavaan@0.6.6:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
