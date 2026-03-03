# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeeprstudio(RPackage):
	"""Seamless Language Translation in 'RStudio' using 'DeepL' API and
'Rstudioapi'

	Enhancing cross-language compatibility within the 'RStudio' environment and supporting seamless language understanding, 
    the 'deepRstudio' package leverages the power of the 'DeepL' API (see <https://www.deepl.com/docs-api>) to enable seamless, fast, 
    accurate, and affordable translation of code comments, documents, and text. This package offers the ability to translate selected text 
    into English (EN), as well as from English into various languages, namely Japanese (JA), Chinese (ZH), Spanish (ES), 
    French (FR), Russian (RU), Portuguese (PT), and Indonesian (ID). With much of the text being written in English, the emphasis 
    is on compatibility from English. It is also designed for developers working on multilingual projects and data analysts collaborating 
    with international teams, simplifying the translation process and making code more accessible and comprehensible to people with 
    diverse language backgrounds. This package uses the 'rstudioapi' package and 'DeepL' API, and is simply implemented, executed 
    from addins or via shortcuts on 'RStudio'. With just a few steps, content can be translated between supported languages, promoting better 
    collaboration and expanding the global reach of work. The functionality of this package works only on 'RStudio' using 'rstudioapi'.
	"""
	
	homepage = "https://kumes.github.io/deepRstudio/"
	cran = "deepRstudio" 

	version("0.0.9", md5="961481ef1022fa9d03e9e86f702c0173")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
