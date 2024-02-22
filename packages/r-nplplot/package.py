# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNplplot(RPackage):
	"""Plotting Linkage and Association Results

	Provides routines for plotting
      linkage and association results along a chromosome,
      with marker names displayed along the top border.
      There are also routines for generating BED and BedGraph
      custom tracks for viewing in the UCSC genome browser.
      The data reformatting program Mega2 uses this
      package to plot output from a variety of
      programs.  
	"""
	
	homepage = "https://watson.hgen.pitt.edu/register/"
	cran = "nplplot" 

	version("4.7", md5="8221a117a040c03fd3867a0ff7750d77")

