# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllomr(RPackage):
	"""Removing Allometric Effects of Body Size in Morphological
Analysis

	Implementation of the technique of Lleonart et al. 
    (2000) <doi:10.1006/jtbi.2000.2043> to scale body measurements 
    that exhibit an allometric growth. This procedure is a theoretical 
    generalization of the technique used by Thorpe 
    (1975) <doi:10.1111/j.1095-8312.1975.tb00732.x> and
    Thorpe (1976) <doi:10.1111/j.1469-185X.1976.tb01063.x>.
	"""
	
	cran = "allomr" 

	version("0.3.0", md5="e494983a577cdaf9326129a0b0343af5")

