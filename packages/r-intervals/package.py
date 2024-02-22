# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntervals(RPackage):
	"""Tools for working with and comparing sets of points and intervals."""

	cran = "intervals"

	version("0.15.4", md5="3ae67facc1528d3626057793aa553924")

	depends_on("r@2.9:", type=("build", "run"))
