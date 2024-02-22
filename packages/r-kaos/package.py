# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKaos(RPackage):
	"""Encoding of Sequences Based on Frequency Matrix Chaos Game
Representation

	Sequences encoding by using the chaos game representation.
    Löchel et al. (2019) <doi:10.1093/bioinformatics/btz493>.
	"""
	
	cran = "kaos" 

	version("0.1.2", md5="20724b3f0968858cd634c2bd212df933")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
