# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmcplite(RPackage):
	"""Lightweight Graph Based Multiple Comparison Procedures

	A lightweight fork of 'gMCP' with functions for graphical
    described multiple test procedures introduced in
    Bretz et al. (2009) <doi:10.1002/sim.3495> and
    Bretz et al. (2011) <doi:10.1002/bimj.201000239>.
    Implements a flexible function using 'ggplot2' to create
    multiplicity graph visualizations.
    Contains instructions of multiplicity graph and graphical testing for
    group sequential design, described in
    Maurer and Bretz (2013) <doi:10.1080/19466315.2013.807748>,
    with necessary unit testing using 'testthat'.
	"""
	
	homepage = "https://merck.github.io/gMCPLite/"
	cran = "gMCPLite" 

	version("0.1.5", md5="682b8bb3a9cef0e18978dc358444b707")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
