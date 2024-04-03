# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYulabUtils(RPackage):
	"""Supporting Functions for Packages Maintained by 'YuLab-SMU'.

	Miscellaneous functions commonly used by 'YuLab-SMU'."""

	cran = "yulab.utils"
	version("0.0.6", sha256="973a51b8d1284060aec34e94849eea6783439dbcbf85083dd4f1a5df4f927b25")
	version("0.0.5", sha256="6ecd4dc5dae40e86b7a462fdac3ab8c0b276dcae5a284eb43390a05b01e3056b")
	version("0.0.4", sha256="38850663de53a9166b8e85deb85be1ccf1a5b310bbe4355f3b8bc823ed1b49ae")
	version("0.1.4", md5="67a4fe9a184067fb6d2dff56577e79c7")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
