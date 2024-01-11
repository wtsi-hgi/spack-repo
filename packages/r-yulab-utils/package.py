# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYulabUtils(RPackage):
	"""Supporting Functions for Packages Maintained by 'YuLab-SMU'.

	Miscellaneous functions commonly used by 'YuLab-SMU'."""

	cran = "yulab.utils"

	version("0.1.0", md5="0dc7aa17f969d84a3f930bbfe2d783cb")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

