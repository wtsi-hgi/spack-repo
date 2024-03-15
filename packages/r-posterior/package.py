# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPosterior(RPackage):
	"""Tools for Working with Posterior Distributions.

	Provides useful tools for both users and developers of packages for
	fitting Bayesian models or working with output from Bayesian models. The
	primary goals of the package are to: (a) Efficiently convert between many
	different useful formats of draws (samples) from posterior or prior
	distributions. (b) Provide consistent methods for operations commonly
	performed on draws, for example, subsetting, binding, or mutating draws.
	(c) Provide various summaries of draws in convenient formats. (d) Provide
	lightweight implementations of state of the art posterior inference
	diagnostics. References: Vehtari et al. (2021) <doi:10.1214/20-BA1221>."""

	cran = "posterior"

	license("BSD-3-Clause")

	version("1.5.0", md5="16f82217acab513b24fa696984ac6ca8")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
	depends_on("r-tensora", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-distributional", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
