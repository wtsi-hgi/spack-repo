# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTitrationcurves(RPackage):
	"""Acid/Base, Complexation, Redox, and Precipitation Titration
Curves

	A collection of functions to plot acid/base titration 
    curves (pH vs. volume of titrant), complexation titration curves 
    (pMetal vs. volume of EDTA), redox titration curves (potential 
    vs.volume of titrant), and precipitation titration curves (either 
    pAnalyte or pTitrant vs. volume of titrant). Options include the 
    titration of mixtures, the ability to overlay two or more 
    titration curves, and the ability to show equivalence points.
	"""
	
	cran = "titrationCurves" 

	version("0.1.0", md5="42ff3398668d5159b9b0221b5c1d04d9")

