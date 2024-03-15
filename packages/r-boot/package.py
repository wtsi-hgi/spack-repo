# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoot(RPackage):
	"""Bootstrap Functions (Originally by Angelo Canty for S).

	Functions and datasets for bootstrapping from the book "Bootstrap Methods
	and Their Application" by A. C. Davison and D. V. Hinkley (1997, CUP),
	originally written by Angelo Canty for S."""

	cran = "boot"

	license("custom")

	version("1.3-30", md5="604cd66b2ee2b7c0718d6c34bd277f7a")

	depends_on("r@3:", type=("build", "run"))
