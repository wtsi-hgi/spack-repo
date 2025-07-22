# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYulabUtils(RPackage):
	"""Supporting Functions for Packages Maintained by 'YuLab-SMU'.

	Miscellaneous functions commonly used by 'YuLab-SMU'."""

	cran = "yulab.utils"
	version("0.2.0", sha256="e79cebefb1439ed68e2f9e613c3dd54230ad3b8a659792b2831dd57fb7105d6a")
	version("0.1.9", sha256="d958877ee9b1bebedeb6e3bb5f19e8df6dce85eb637a89b0d4a583ee60bf3e9f")
	version("0.1.8", sha256="1c492439f7083d67cebead1b3504f781f126f741642a462519bb2818896912b6")
	version("0.1.7", sha256="03cf0afae82de40218a00aed7448a9186db049ba8e298a12d027686237945f60")
	version("0.1.6", sha256="589be7ad1425f7d84dc3748f352fc432e494edb725209c05e28ca2a44f34beec")
	version("0.1.5", sha256="26e272494552777365259155ec52cf5ef6077b2fc3902b23f0812983f0f9f7f5")
	version("0.1.4", sha256="32d4e1b0bfe94b9c051615e65d90fc2bd14e1d6019706cbc483f84c3cd8d3154")
	version("0.1.3", sha256="5b7a62903d2e958284e4b2499acdc659a438cbc8541c173d1fff9888444b027a")
	version("0.1.2", sha256="9aa1999db2bd0f49a8f39ba15206e25c377c25f0094e6568477b82c1ac23555e")
	version("0.1.1", sha256="08ef5888ee341ee72702bc21c694e182c23b8c56b75287adf14d4ae0a7253e64")
	version("0.1.0", sha256="ef4fa9fc7e5fd458f84e0337cd08fd66961cb18be4508c59aa480d715e1fba10")
	version("0.0.9", sha256="9626f073d9c47a8ea6ac7fef5fadf1a0c405589376a5ffeeb9a93c5d3b490579")
	version("0.0.8", sha256="deb01c18e61ac9c7d3eaed88de855a8ab4968998c558708c2a6bebc86fcf62ad")
	version("0.0.7", sha256="e914ea30cd471e8762c91d1c4f2a4740956f278f48208c8fab274941be815d9a")
	version("0.0.6", sha256="973a51b8d1284060aec34e94849eea6783439dbcbf85083dd4f1a5df4f927b25")
	version("0.0.5", sha256="6ecd4dc5dae40e86b7a462fdac3ab8c0b276dcae5a284eb43390a05b01e3056b")
	version("0.0.4", sha256="38850663de53a9166b8e85deb85be1ccf1a5b310bbe4355f3b8bc823ed1b49ae")
	version("0.0.2", sha256="b86860bf183ea193f81da77cffa7181a6562aa2035ef2dae39fa1193c13458c1")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"), when="@0.1.6:")
