# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKs(RPackage):
	"""Kernel Smoothing.

	Kernel smoothers for univariate and multivariate data, including densities,
	density derivatives, cumulative distributions, clustering, classification,
	density ridges, significant modal regions, and two-sample hypothesis tests.
	Chacon & Duong (2018) <doi:10.1201/9780429485572>."""

	cran = "ks"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("1.14.2", md5="895115f86f71e1c4694a8279e5445083")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fnn@1.1:", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-kernsmooth@2.22:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-multicool", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.0:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
