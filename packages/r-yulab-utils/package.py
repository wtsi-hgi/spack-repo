# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYulabUtils(RPackage):
	"""Supporting Functions for Packages Maintained by 'YuLab-SMU'.

	Miscellaneous functions commonly used by 'YuLab-SMU'."""

	cran = "yulab.utils"
	version("0.2.4", sha256="437055d75f7e81d1afd403c0eaae34780a8baf779f01fc5ef0b4b17e45407b81")
	version("0.2.3", sha256="11b2a402a7fbf66f655315784a2468e061eaae7fb18ac7ef634f829aa05e7caf")
	version("0.1.6", sha256="589be7ad1425f7d84dc3748f352fc432e494edb725209c05e28ca2a44f34beec")
	version("0.1.4", md5="67a4fe9a184067fb6d2dff56577e79c7")
	version("0.0.6", sha256="973a51b8d1284060aec34e94849eea6783439dbcbf85083dd4f1a5df4f927b25")
	version("0.0.5", sha256="6ecd4dc5dae40e86b7a462fdac3ab8c0b276dcae5a284eb43390a05b01e3056b")
	version("0.0.4", sha256="38850663de53a9166b8e85deb85be1ccf1a5b310bbe4355f3b8bc823ed1b49ae")

	depends_on("r@4.2:", type=("build", "run"), when="@0.2.0:")
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"), when="@:0.1.4")
	depends_on("r-httr2", type=("build", "run"), when="@0.1.6")
	depends_on("r-rappdirs", type=("build", "run"), when="@0.2.1:")
	depends_on("r-rlang", type=("build", "run"))
