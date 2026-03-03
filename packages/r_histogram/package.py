# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistogram(RPackage):
	"""Construction of Regular and Irregular Histograms with Different
Options for Automatic Choice of Bins

	Automatic construction of regular and irregular histograms as described in Rozenholc/Mildenberger/Gather (2010).
	"""
	
	cran = "histogram" 

	version("0.0-25", md5="b37514dd2918e1412bb4ca0798550722")

