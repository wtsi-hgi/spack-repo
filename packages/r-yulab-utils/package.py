# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYulabUtils(RPackage):
	"""Supporting Functions for Packages Maintained by 'YuLab-SMU'.

	Miscellaneous functions commonly used by 'YuLab-SMU'."""

	cran = "yulab.utils"

	version("0.1.4", md5="67a4fe9a184067fb6d2dff56577e79c7")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
