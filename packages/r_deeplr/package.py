# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeeplr(RPackage):
	"""Interface to the 'DeepL' Translation API

	A wrapper for the 'DeepL' Pro API <https://www.deepl.com/docs-api>, a web service
    for translating texts between different languages. A DeepL API developer account is required
    to use the service (see <https://www.deepl.com/pro#developer>).
	"""
	
	homepage = "https://www.deepl.com/translator"
	cran = "deeplr" 

	version("2.0.1", md5="c16a20429a8a829214db41985faa3fca")

	depends_on("r-utf8", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
