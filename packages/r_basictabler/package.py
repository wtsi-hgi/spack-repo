# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasictabler(RPackage):
	"""Construct Rich Tables for Output to 'HTML'/'Excel'

	Easily create tables from data 
    frames/matrices.  Create/manipulate tables 
    row-by-row, column-by-column or cell-by-cell.  
    Use common formatting/styling to output 
    rich tables as 'HTML', 'HTML widgets' or to 
    'Excel'. 
	"""
	
	homepage = "http://www.basictabler.org.uk/"
	cran = "basictabler" 

	version("1.0.2", md5="389a502c73a0eff07956ae4c5f62a21b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6@2.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-htmltools@0.3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.8:", type=("build", "run"))
