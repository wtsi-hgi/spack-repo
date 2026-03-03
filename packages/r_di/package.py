# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDi(RPackage):
	"""Deficit Index (DI)

	A set of utilities for calculating the Deficit (frailty) Index (DI) in gerontological studies. 
             The deficit index was first proposed by Arnold Mitnitski and Kenneth Rockwood 
             and represents a proxy measure of aging and also can be served as
             a sensitive predictor of survival. For more information, see 
             (i)"Accumulation of Deficits as a Proxy Measure of Aging" 
             by Arnold B. Mitnitski et al. (2001), 
             The Scientific World Journal 1, <DOI:10.1100/tsw.2001.58>;
             (ii) "Frailty, fitness and late-life mortality in relation to chronological and biological age" 
             by Arnold B Mitnitski et al. (2001), 
             BMC Geriatrics2002 2(1), <DOI:10.1186/1471-2318-2-1>.
	"""
	
	cran = "di" 

	version("1.1.4", md5="f72946d9e6ac90130afdc2c1d50161a7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
