# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFints(RPackage):
	"""Companion to Tsay (2005) Analysis of Financial Time Series

	R companion to Tsay (2005) Analysis of Financial Time
   Series, second edition (Wiley).  Includes data sets, functions and
   script files required to work some of the examples.  Version 0.3-x
   includes R objects for all data files used in the text and script
   files to recreate most of the analyses in chapters 1-3 and 9 plus
   parts of chapters 4 and 11.
	"""
	
	homepage = "https://geobosh.github.io/FinTSDoc/"
	cran = "FinTS" 

	version("0.4-9", md5="be99778a7d783224b05f108f98ae810a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
