# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexexamrandomizer(RPackage):
	"""Personalizes and Randomizes Exams Written in 'LaTeX'

	Randomizing exams with 'LaTeX'.
    If you can compile your main document with 'LaTeX', the program should be able to compile the randomized
    versions without much extra effort when creating the document.
	"""
	
	homepage = "https://github.com/alexrecuenco/TexExamRandomizer"
	cran = "TexExamRandomizer" 

	version("1.2.7", md5="dc7a3d5fe5cc7c222d6725f5477ed8e6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
