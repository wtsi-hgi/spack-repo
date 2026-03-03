# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIspd(RPackage):
	"""Incomplete Split-Plot Designs

	A collection of several functions related to construction and analysis of incomplete split-plot designs. The package contains functions to obtain  and analyze incomplete split-plot designs for three kinds of situations namely (i) when blocks are complete with respect to main plot treatments and main plots are incomplete with respect to subplot treatments, (ii) when blocks are  incomplete with respect to main plot treatments and main plots are complete with respect to subplot treatments and (iii) when blocks are incomplete with respect to main plot treatments and main plots are incomplete with respect to subplot treatments.  
	"""
	
	cran = "ispd" 

	version("0.2", md5="b3d88a442bd238c47ecb51a171c3c1d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ibd", type=("build", "run"))
