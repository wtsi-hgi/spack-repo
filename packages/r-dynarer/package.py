# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynarer(RPackage):
	"""Bringing the Power of 'Dynare' to 'R', 'R Markdown', and
'Quarto'

	It allows running 'Dynare' program from base R, R Markdown and Quarto. 'Dynare' is a software platform for handling a wide class of economic models, in particular dynamic stochastic general equilibrium ('DSGE') and overlapping generations ('OLG') models.  This package does not only integrate R and Dynare but also serves as a 'Dynare' Knit-Engine for 'knitr' package. The package requires 'Dynare' (<https://www.dynare.org/>) and 'Octave' (<https://www.octave.org/download.html>).  Write all your 'Dynare' commands in R or R Markdown chunk.
	"""
	
	homepage = "https://CRAN.R-project.org/package=DynareR"
	cran = "DynareR" 

	version("0.1.4", md5="258a578f7c3ac15761877c8fb338bcdc")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("octave", type=("build", "link", "run"))
