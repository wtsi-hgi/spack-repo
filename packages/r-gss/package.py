# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGss(RPackage):
	"""General Smoothing Splines.

	A comprehensive package for structural multivariate function estimation
	using smoothing splines."""

	cran = "gss"

	license("GPL-2.0-or-later")

	version("2.2-7", md5="e86db9bf39e0d151e7242e42c9b6f7ca")

	depends_on("r@3:", type=("build", "run"))
