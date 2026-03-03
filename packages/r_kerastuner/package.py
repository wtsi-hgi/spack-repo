# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKerastuner(RPackage):
	"""Interface to 'Keras Tuner'

	'Keras Tuner' <https://keras-team.github.io/keras-tuner/> is a hypertuning framework made for humans. 
             It aims at making the life of AI practitioners, hypertuner 
             algorithm creators and model designers as simple as possible by 
             providing them with a clean and easy to use API for hypertuning. 
             'Keras Tuner' makes moving from a base model to a hypertuned one quick and 
             easy by only requiring you to change a few lines of code.
	"""
	
	homepage = "https://github.com/EagerAI/kerastuneR/"
	cran = "kerastuneR" 

	version("0.1.0.6", md5="c4026a73d84e29cde6245eb2b8dda1be")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-tidyjson", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-echarts4r", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("py-tensorflow@2.0:", type=("build", "link", "run"))
