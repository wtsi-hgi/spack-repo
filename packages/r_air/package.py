# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAir(RPackage):
	"""AI Assistant to Write and Understand R Code

	An R console utility that lets you ask R related questions to the
    'OpenAI' large language model. It can answer 'how-to()' questions by  
    providing code, and 'whatis()' questions by explaining what given code does.
    You must provision your own key for the 'OpenAI' API 
    <https://platform.openai.com/docs/api-reference>.
	"""
	
	homepage = "https://github.com/soumyaray/air"
	cran = "air" 

	version("0.2.2", md5="cf8f27dbc5d9bfbf02bb7644863a445c")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
