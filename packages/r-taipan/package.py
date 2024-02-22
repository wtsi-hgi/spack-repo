# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaipan(RPackage):
	"""Tool for Annotating Images in Preparation for Analysis

	A tool to help create shiny apps for selecting and annotating 
    elements of images. Users must supply images, questions, and answer
    choices. The user interface is a dynamic shiny app, that displays the images
    and questions and answer choices. The data generated can be saved to a
    file that can be used for subsequent analysis. The original purpose was to
    annotate still images from tennis video for face recognition and emotion 
    detection purposes.
	"""
	
	homepage = "https://github.com/srkobakian/taipan"
	cran = "taipan" 

	version("0.1.2", md5="26d503b2fcff69cb8370547c50fe96fc")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
