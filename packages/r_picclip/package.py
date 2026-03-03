# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPicclip(RPackage):
	"""Paste Box Input for 'Shiny'

	Provides a 'Shiny' input widget, pasteBoxInput, 
    that allows users to paste images directly into a 'Shiny' 
    application. The pasted images are captured as Base64 
    encoded strings and can be used within the application 
    for various purposes, such as display or further processing. 
    This package is particularly useful for applications that 
    require easy and quick image uploads without the need for 
    traditional file selection dialog boxes.
	"""
	
	homepage = "https://github.com/deppemj/picClip"
	cran = "picClip" 

	version("0.1.0", md5="c2f38869d0bbfd4f6562b68d7223d797")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
