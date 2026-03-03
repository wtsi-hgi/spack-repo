# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdoc(RPackage):
	"""Colourised R Documentation

	Extends tools::Rd2txt() by adding customisable text and colour formatting to R documentation 
    contents. If used from a terminal, output will be displayed via file.show() otherwise contents
    will be printed in sections. Also provides stand-in replacements for ?() and help().
	"""
	
	homepage = "https://github.com/mdequeljoe/rdoc"
	cran = "rdoc" 

	version("0.1.0", md5="bb4d4f2aa5765832f5695bead89c9304")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-prettycode", type=("build", "run"))
