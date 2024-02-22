# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenai(RPackage):
	"""Generative Artificial Intelligence

	Utilizing Generative Artificial Intelligence models like 'GPT-4' and 'Gemini Pro' as coding and writing assistants for 'R' users. Through these models, 'GenAI' offers a variety of functions, encompassing text generation, code optimization, natural language processing, chat, and image interpretation. The goal is to aid 'R' users in streamlining laborious coding and language processing tasks.
	"""
	
	homepage = "https://genai.gd.edu.kg/"
	cran = "GenAI" 

	version("0.2.0", md5="678f493e49cf41b608ce16ead96583bc")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-listenv", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
