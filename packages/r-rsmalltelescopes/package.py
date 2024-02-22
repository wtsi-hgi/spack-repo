# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsmalltelescopes(RPackage):
	"""Empirical Small Telescopes Analysis

	We provide functions to perform an empirical small telescopes
    analysis. This package contains 2 functions, SmallTelescopes() and 
    EstimatePower(). Users only need to call SmallTelescopes() to conduct 
    the analysis. For more information on small telescopes analysis see
    Uri Simonsohn (2015) <doi:10.1177/0956797614567341>.
	"""
	
	cran = "RSmallTelescopes" 

	version("1.0.4", md5="eff9497485fbfa2624a184b0665d1e9b")

