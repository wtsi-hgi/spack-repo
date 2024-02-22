# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRyandextranslate(RPackage):
	"""R Interface to Yandex Translate API

	'Yandex Translate' (https://translate.yandex.com/) is a statistical machine translation system.
	The system translates separate words, complete texts, and webpages.
	This package can be used to detect language from text and to translate it to supported target language.
	For more info: https://tech.yandex.com/translate/doc/dg/concepts/About-docpage/ .
	"""
	
	homepage = "https://github.com/mukul13/RYandexTranslate"
	cran = "RYandexTranslate" 

	version("1.0", md5="088770707832f98e68d9ec6820e2d961")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
