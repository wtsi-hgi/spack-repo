# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetpass(RPackage):
	"""Masked User Input

	A micro-package for reading "passwords", i.e.  reading
    user input with masking, so that the input is not displayed as it 
    is typed.  Currently we have support for 'RStudio', the command line
    (every OS), and any platform where 'tcltk' is present.  
	"""
	
	homepage = "https://github.com/wrathematics/getPass"
	cran = "getPass" 

	version("0.2-4", md5="4d5b96287de26d2bf021c940965d76a3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
