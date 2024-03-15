# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQqconf(RPackage):
	"""Creates Simultaneous Testing Bands for QQ-Plots.

	Provides functionality for creating Quantile-Quantile (QQ) and
	Probability-Probability (PP) plots with simultaneous testing bands to asses
	significance of sample deviation from a reference distribution."""

	cran = "qqconf"

	license("GPL-3.0-only")

	version("1.3.2", md5="978d24f76cbdf61ad8b4ff4299a9d839")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass@7.3.50:", type=("build", "run"))
	depends_on("r-robustbase@0.93.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("fftw@3.1.2:", type=("build", "link", "run"))
	depends_on("pkgconfig", type=("build", "link", "run"))
