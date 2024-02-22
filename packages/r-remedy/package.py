# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemedy(RPackage):
	"""'RStudio' Addins to Simplify 'Markdown' Writing

	An 'RStudio' addin providing shortcuts for writing in 'Markdown'. This package provides a series of 
             functions that allow the user to be more efficient when using 'Markdown'. For example, you can select 
             a word, and put it in bold or in italics, or change the alignment of elements inside you Rmd. The idea
             is to map all the functionalities from 'remedy' on keyboard shortcuts, so that it provides an interface 
             close to what you can find in any other text editor. 
	"""
	
	homepage = "https://github.com/ThinkR-open/remedy"
	cran = "remedy" 

	version("0.1.0", md5="9622ffb2cf6817c10345b8e300613749")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
