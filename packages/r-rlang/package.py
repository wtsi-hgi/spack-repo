# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlang(RPackage):
	"""Functions for Base Types and Core R and 'Tidyverse' Features.

	A toolbox for working with base types, core R features like the condition
	system, and core 'Tidyverse' features like tidy evaluation."""

	cran = "rlang"

	license("MIT")

	version("1.1.3", md5="cf4c3b1270d4d047d5c8104da270ba30")

	depends_on("r@3.5:", type=("build", "run"))
