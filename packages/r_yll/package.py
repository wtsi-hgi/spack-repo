# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYll(RPackage):
	"""Compute Expected Years of Life Lost (YLL) and Average YLL

	Compute the standard expected years of life lost (YLL),
    as developed by the Global Burden of Disease Study
    (Murray, C.J., Lopez, A.D. and World Health Organization, 1996).
    The YLL is based on comparing the age of death to an external standard life
    expectancy curve. It also computes the average YLL, which highlights premature
    causes of death and brings attention to preventable deaths
    (Aragon et al., 2008).
	"""
	
	homepage = "https://github.com/AntoineSoetewey/yll"
	cran = "yll" 

	version("1.0.0", md5="a9eb945c6dae1052e3a6908003ed466b")

	depends_on("r@3.1:", type=("build", "run"))
