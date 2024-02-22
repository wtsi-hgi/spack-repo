# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPinyin(RPackage):
	"""Convert Chinese Characters into Pinyin, Sijiao, Wubi or Other
Codes

	Convert Chinese characters into Pinyin (the official romanization system for Standard Chinese in mainland China, Malaysia, Singapore, and Taiwan. See <https://en.wikipedia.org/wiki/Pinyin> for details), Sijiao (four or five numerical digits per character. See <https://en.wikipedia.org/wiki/Four-Corner_Method>.), Wubi (an input method with five strokes. See <https://en.wikipedia.org/wiki/Wubi_method>) or user-defined codes.
	"""
	
	homepage = "https://github.com/pzhaonet/pinyin"
	cran = "pinyin" 

	version("1.1.6", md5="e50eec402c94624440ddf67f93c19e3d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
