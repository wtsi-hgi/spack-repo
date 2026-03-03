# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoice(RPackage):
	"""Tools for Voice Analysis, Speaker Recognition and Mood Inference

	Tools for voice analysis, speaker recognition and mood inference. 
    Gathers 'R' and 'Python' tools to solve problems concerning voice and audio 
    in general.
	"""
	
	homepage = "https://github.com/filipezabala/voice"
	cran = "voice" 

	version("0.4.21", md5="95a01033af9e1de74ac704a5d970fb28")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-wrassp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
