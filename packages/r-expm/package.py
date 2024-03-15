# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpm(RPackage):
	"""Matrix Exponential, Log, 'etc'.

	Computation of the matrix exponential, logarithm, sqrt, and related
	quantities."""

	cran = "expm"

	license("GPL-2.0-or-later")

	version("0.999-9", md5="6ae969bc1a952491529805f79477a056")

	depends_on("r-matrix", type=("build", "run"))
