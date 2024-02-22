# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotscale(RPackage):
	"""Scale Graphics Devices Using Plot Dimensions

	Figures rendered on graphics devices are usually 
 rescaled to fit pre-determined device dimensions. 'plotscale' 
 implements the reverse: desired plot dimensions are specified 
 and device dimensions are calculated to accommodate marginal
 material, giving consistent proportions for plot elements.
 Default methods support grid graphics such as lattice and ggplot.
 See "example('devsize')" and "vignette('plotscale')".
	"""
	
	cran = "plotscale" 

	version("0.1.6", md5="51b222c1202ad036e8287fdb374f0fc6")

