# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrintr(RPackage):
	"""Automatically Print R Objects to Appropriate Formats According
to the 'knitr' Output Format

	Extends the S3 generic function knit_print() in 'knitr'
    to automatically print some objects using an appropriate format such as
    Markdown or LaTeX. For example, data frames are automatically printed as
    tables, and the help() pages can also be rendered in 'knitr' documents.
	"""
	
	homepage = "https://yihui.org/printr/"
	cran = "printr" 

	version("0.3", md5="2c81cb77598873663ee04e342ff5aa64")

	depends_on("r-knitr@1.31:", type=("build", "run"))
