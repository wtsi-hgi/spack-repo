# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscstts(RPackage):
	"""R Client for the Microsoft Cognitive Services 'Text-to-Speech'
REST API

	R Client for the Microsoft Cognitive Services 
  'Text-to-Speech' REST API, including voice synthesis. A valid account 
  must be registered at the Microsoft Cognitive Services website 
  <https://azure.microsoft.com/services/cognitive-services/> in order to 
  obtain a (free) API key. Without an API key, this package will not 
  work properly.
	"""
	
	homepage = "https://github.com/muschellij2/mscstts"
	cran = "mscstts" 

	version("0.6.3", md5="90a9dacc6fea89086c8aab4614032027")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
