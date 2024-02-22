# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglelanguager(RPackage):
	"""Call Google's 'Natural Language' API, 'Cloud Translation' API,
'Cloud Speech' API and 'Cloud Text-to-Speech' API

	Call 'Google Cloud' machine learning APIs for text and speech tasks.
  Call the 'Cloud Translation' API <https://cloud.google.com/translate/> for detection 
  and translation of text, the 'Natural Language' API <https://cloud.google.com/natural-language/> to 
  analyse text for sentiment, entities or syntax, the 'Cloud Speech' API 
  <https://cloud.google.com/speech/> to transcribe sound files to text and 
  the 'Cloud Text-to-Speech' API <https://cloud.google.com/text-to-speech/> to turn text 
  into sound files.
	"""
	
	homepage = "http://code.markedmondson.me/googleLanguageR/"
	cran = "googleLanguageR" 

	version("0.3.0", md5="3b3c818332802f601c81836fa825bf8d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-googleauthr@1.1.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
