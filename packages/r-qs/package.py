# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQs(RPackage):
	"""Quick Serialization of R Objects.

	Provides functions for quickly writing and reading any R object to and from
	disk."""

	cran = "qs"

	maintainers("dorton21")

	license("GPL-3.0-only")

	version("0.26.1", md5="ee0fad99d74c0798fcea6659f988b2d1")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rapiserialize", type=("build", "run"))
	depends_on("r-stringfish", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
