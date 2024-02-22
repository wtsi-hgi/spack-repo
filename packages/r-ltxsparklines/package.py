# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtxsparklines(RPackage):
	"""Lightweight Sparklines for a LaTeX Document

	Sparklines are small plots (about one line of text high),
  made popular by Edward Tufte.  This package is the interface from R
  to the LaTeX package sparklines by Andreas Loeffer and Dan Luecking
  (<http://www.ctan.org/pkg/sparklines>).  It can work with Sweave or
  knitr or other engines that produce TeX.  The package can be used to
  plot vectors, matrices, data frames, time series (in ts or zoo format).
	"""
	
	homepage = "https://github.com/borisveytsman/ltxsparklines"
	cran = "ltxsparklines" 

	version("1.1.3", md5="30eba39839eeb5c1666cca5f655a30ab")

