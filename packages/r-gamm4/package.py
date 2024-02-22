# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamm4(RPackage):
	"""Generalized Additive Mixed Models using 'mgcv' and 'lme4'.

	Estimate generalized additive mixed models via a version of function gamm()
	from 'mgcv', using 'lme4' for estimation."""

	cran = "gamm4"

	version("0.2-6", md5="dff478c7c80f51c0356df39347fdf9f5", url="https://cran.r-project.org/src/contrib/gamm4_0.2-6.tar.gz")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
	depends_on("r-mgcv@1.7.23:", type=("build", "run"))
