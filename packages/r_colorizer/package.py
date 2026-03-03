# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorizer(RPackage):
	"""Colorize Old Images Using the 'DeOldify' Image Colorization API

	Call the 'DeOldify' <https://github.com/jantic/DeOldify> image
    colorization API on 'DeepAI'<https://deepai.org/machine-learning-model/colorizer>
    to colorize black and white images.
	"""
	
	homepage = "https://github.com/zumbov2/colorizer"
	cran = "colorizer" 

	version("0.1.0", md5="025e99f1f8a5b691381b0537ec5aa558")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
