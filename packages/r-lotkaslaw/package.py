# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLotkaslaw(RPackage):
	"""Runs Lotka's Law which is One of the Special Applications of
Zipf's Law

	Running Lotka's Law following Pao (1985)(DOI: 10.1016/0306-4573(85)90055-X). The Law is based around the proof that the number of authors making n contributions is about 1/n^{a} of those making one contribution.
	"""
	
	cran = "LotkasLaw" 

	version("0.0.1.0", md5="e9d04310e82ea2671202dd2ba9d6a7f7")

	depends_on("r@3.1.1:", type=("build", "run"))
