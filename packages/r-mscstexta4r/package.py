# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscstexta4r(RPackage):
	"""R Client for the Microsoft Cognitive Services Text Analytics
REST API

	R Client for the Microsoft Cognitive Services Text Analytics
    REST API, including Sentiment Analysis, Topic Detection, Language Detection,
    and Key Phrase Extraction. An account MUST be registered at the Microsoft
    Cognitive Services website <https://www.microsoft.com/cognitive-services/>
    in order to obtain a (free) API key. Without an API key, this package will
    not work properly.
	"""
	
	homepage = "https://github.com/philferriere/mscstexta4r"
	cran = "mscstexta4r" 

	version("0.1.2", md5="3851d6f71bbf699d01c6d64871ff3e35")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
