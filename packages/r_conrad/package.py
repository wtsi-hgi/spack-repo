# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConrad(RPackage):
	"""Client for the Microsoft's 'Cognitive Services Text to Speech
REST' API

	Convert text into synthesized speech and get a list of supported voices for a region. 
    Microsoft's 'Cognitive Services Text to Speech REST' API <https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/rest-text-to-speech?tabs=streaming>  
    supports neural text to speech voices, which support specific languages and dialects that are identified by locale. 
	"""
	
	homepage = "https://github.com/fhdsl/conrad"
	cran = "conrad" 

	version("1.0.0", md5="c99cbd97cd4ad8c8069e1fe75f60d5aa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
