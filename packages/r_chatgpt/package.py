# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChatgpt(RPackage):
	"""Interface to 'ChatGPT' from R

	'OpenAI's 'ChatGPT' <https://chat.openai.com/> coding assistant for 'RStudio'. A set 
  of functions and 'RStudio' addins that aim to help the R developer in tedious coding tasks.
	"""
	
	homepage = "https://github.com/jcrodriguez1989/chatgpt"
	cran = "chatgpt" 

	version("0.2.3", md5="d665ffe2798ea1fe60813369a6f55231")

	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
