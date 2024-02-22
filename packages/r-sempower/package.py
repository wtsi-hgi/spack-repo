# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSempower(RPackage):
	"""Power Analyses for SEM

	Provides a-priori, post-hoc, and compromise power-analyses
    for structural equation models (SEM).
	"""
	
	homepage = "https://github.com/moshagen/semPower"
	cran = "semPower" 

	version("2.1.0", md5="ef38f7e51a0a3b378a26d3c0ad232058")

