# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernscr(RPackage):
	"""Kernel Machine Score Test for Semi-Competing Risks

	Kernel Machine Score Test for Pathway Analysis in the Presence of 
    Semi-Competing Risks. Method is detailed in: Neykov, Hejblum & Sinnott (2018) 
    <doi: 10.1177/0962280216653427>.
	"""
	
	cran = "kernscr" 

	version("1.0.6", md5="6c27d678361985fb759139c140aa907e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
