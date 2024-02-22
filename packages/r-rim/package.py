# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRim(RPackage):
	"""Interface to 'Maxima', Enabling Symbolic Computation

	An interface to the powerful and fairly complete computer algebra system 'Maxima'.
    It can be used to start and control 'Maxima' from within R by entering 'Maxima' commands. 
    Results from 'Maxima' can be parsed and evaluated in R. 
    It facilitates outputting results from 'Maxima' in 'LaTeX' and 'MathML'. 
    2D and 3D plots can be displayed directly. 
    This package also registers a 'knitr'-engine enabling 'Maxima' code chunks 
    to be written in 'RMarkdown' documents.
	"""
	
	homepage = "https://rcst.github.io/rim/"
	cran = "rim" 

	version("0.6.4", md5="3475c12828b2b42277c4caa0560d53de")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-globaloptions", type=("build", "run"))
