# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RText2speech(RPackage):
	"""Text to Speech Conversion

	Converts text into speech using various text-to-speech (TTS) engines and provides an unified interface for accessing their functionality.
  With this package, users can easily generate audio files of spoken words, phrases, or sentences from plain text data. The package supports multiple TTS engines, 
  including Google's 'Cloud Text-to-Speech API', 'Amazon Polly', Microsoft's 'Cognitive Services Text to Speech REST API',  and a free TTS engine called 'Coqui TTS'.
	"""
	
	homepage = "https://github.com/jhudsl/text2speech"
	cran = "text2speech" 

	version("1.0.0", md5="1563e73e74949ffd014b243529099d77")

	depends_on("r-aws-signature", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-googleauthr", type=("build", "run"))
	depends_on("r-googlelanguager", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-conrad", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
