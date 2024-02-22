# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscsweblm4r(RPackage):
	"""R Client for the Microsoft Cognitive Services Web Language Model
REST API

	R Client for the Microsoft Cognitive Services Web Language Model
    REST API, including Break Into Words, Calculate Conditional
    Probability, Calculate Joint Probability, Generate Next Words, and List
    Available Models. A valid account MUST be registered at the Microsoft
    Cognitive Services website <https://www.microsoft.com/cognitive-services/>
    in order to obtain a (free) API key. Without an API key, this package will
    not work properly.
	"""
	
	homepage = "https://github.com/philferriere/mscsweblm4r"
	cran = "mscsweblm4r" 

	version("0.1.2", md5="fb6eff1c68da1970a4af9fb5a094f25f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
