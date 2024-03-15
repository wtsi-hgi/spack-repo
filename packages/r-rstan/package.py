# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstan(RPackage):
	"""R Interface to Stan.

	User-facing R functions are provided to parse, compile, test, estimate, and
	analyze Stan models by accessing the header-only Stan library provided by
	the 'StanHeaders' package. The Stan project develops a probabilistic
	programming language that implements full Bayesian statistical inference
	via Markov Chain Monte Carlo, rough Bayesian inference via variational
	approximation, and (optionally penalized) maximum likelihood estimation via
	optimization. In all three cases, automatic differentiation is used to
	quickly and accurately evaluate gradients without burdening the user with
	the need to derive the partial derivatives."""

	cran = "rstan"

	license("GPL-3.0-or-later")

	version("2.32.6", md5="93aecb7454d73942e9b0c719b2723505")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stanheaders@2.32:", type=("build", "run"))
	depends_on("r-inline@0.3.19:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
	depends_on("r-loo@2.4.1:", type=("build", "run"))
	depends_on("r-pkgbuild@1.2:", type=("build", "run"))
	depends_on("r-quickjsr", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.4:", type=("build", "run"))
	depends_on("r-bh@1.75.0.0:", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
	depends_on("pandoc", type=("build", "link", "run"))

	conflicts("%gcc@:4.9", when="@2.18:")
