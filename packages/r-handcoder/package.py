# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHandcoder(RPackage):
	"""Text Annotation App

	Shiny-App that allows to annotate vectors of texts to predefined categories by hand. 
	"""
	
	homepage = "https://github.com/liserman/handcodeR/"
	cran = "handcodeR" 

	version("0.1.2", md5="f8d3fa75ca01d4202a70cc29eda69d43")

	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-shinywidgets@0.7.6:", type=("build", "run"))
