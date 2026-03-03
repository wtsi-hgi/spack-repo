# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlp(RPackage):
	"""Discrete Prolate Spheroidal (Slepian) Sequence Regression
Smoothers

	Interface for creation of 'slp' class smoother objects for 
             use in Generalized Additive Models (as implemented by packages 
             'gam' and 'mgcv'). 
	"""
	
	cran = "slp" 

	version("1.0-5", md5="e5a7bf7ac29656296db662a9c4f21f37")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-mgcv@1.7.18:", type=("build", "run"))
