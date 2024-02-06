# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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

	version("0.25.7", md5="0f8d2ea505343d10d02917badd85a100")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rapiserialize", type=("build", "run"))
	depends_on("r-stringfish", type=("build", "run"))
