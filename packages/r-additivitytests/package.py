# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdditivitytests(RPackage):
	"""Additivity Tests in the Two Way Anova with Single Sub-Class
Numbers

	Implementation of the Tukey, Mandel, Johnson-Graybill, LBI, Tusell
    and modified Tukey non-additivity tests.
	"""
	
	homepage = "https://github.com/simecek/additivityTests"
	cran = "additivityTests" 

	version("1.1-4.1", md5="0aa55442e90e17042e1fdb78b29c525c")

