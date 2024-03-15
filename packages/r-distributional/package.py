# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistributional(RPackage):
	"""Functions for Base Types and Core R and 'Tidyverse' Features.

	Vectorised distribution objects with tools for manipulating, visualising,
	and using probability distributions. Designed to allow model prediction
	outputs to return distributions rather than their parameters, allowing
	users to directly interact with predictive distributions in a data-oriented
	workflow. In addition to providing generic replacements for p/d/q/r
	functions, other useful statistics can be computed including means,
	variances, intervals, and highest density regions."""

	cran = "distributional"

	license("GPL-3.0-only")

	version("0.4.0", md5="96a6b3560c947cf6622180d54a85db2b")

	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
