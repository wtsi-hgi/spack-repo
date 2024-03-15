# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringfish(RPackage):
	"""Alt String Implementation.

	Provides an extendable, performant and multithreaded 'alt-string'
	implementation backed by 'C++' vectors and strings."""

	cran = "stringfish"

	maintainers("dorton21")

	license("GPL-3.0-only")

	version("0.16.0", md5="5ca337ca8e7eeed112eb342165a93684")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.18.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
