# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyscselection(RPackage):
	"""Systematic Scenario Selection for Stress Testing

	Quasi-Monte-Carlo algorithm for systematic generation of shock scenarios from an arbitrary multivariate elliptical distribution. The algorithm selects a systematic mesh of arbitrary fineness that approximately evenly covers an isoprobability ellipsoid in d dimensions (Flood, Mark D. & Korenko, George G. (2013) <doi:10.1080/14697688.2014.926018>).
  This package is the 'R' analogy to the 'Matlab' code published by Flood & Korenko in above-mentioned paper.
	"""
	
	cran = "SyScSelection" 

	version("1.0.2", md5="65a3b3c2936357b79b4cb9a413e22efc")

	depends_on("r-pracma", type=("build", "run"))
