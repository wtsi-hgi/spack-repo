# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgmaker(RPackage):
	"""Development Utilities for R Packages.

	This package provides some low-level utilities to use for package
	development. It currently provides managers for multiple package specific
	options and registries, vignette, unit test and bibtex related utilities.
	It serves as a base package for packages like NMF, RcppOctave, doRNG, and
	as an incubator package for other general purposes utilities, that will
	eventually be packaged separately. It is still under heavy development and
	changes in the interface(s) are more than likely to happen."""

	cran = "pkgmaker"

	license("GPL-2.0-or-later")

	version("0.32.10", md5="f193c5771759134ee1c1c063cb7303c3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-registry", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
