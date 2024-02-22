# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpa(RPackage):
	"""Spatio-Temporal Fixation Pattern Analysis

	Spatio-temporal Fixation Pattern Analysis (FPA) is a new method of analyzing eye 
  movement data, developed by Mr. Jinlu Cao under the supervision of Prof. Chen Hsuan-Chih at 
  The Chinese University of Hong Kong, and Prof. Wang Suiping at the South China Normal 
  Univeristy. The package "fpa" is a R implementation which makes FPA analysis much easier. 
  There are four major functions in the package: ft2fp(), get_pattern(), plot_pattern(), and 
  lineplot(). The function ft2fp() is the core function, which can complete all the preprocessing 
  within moments. The other three functions are supportive functions which visualize the eye 
  fixation patterns.
	"""
	
	cran = "fpa" 

	version("1.0", md5="24e33e7f24bf6ae0214c94a79340e4d5")

	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
