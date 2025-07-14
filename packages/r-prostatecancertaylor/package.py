# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancertaylor(RPackage):
	"""Prostate Cancer Data

	A Bioconductor data package for the Taylor et al (2010) dataset.
	"""
	
	bioc = "prostateCancerTaylor"

	version("1.36.0", commit="2597f83d9a4ee25028c97de3a7ca08e6f4fcf504")
	version("1.30.0", commit="095c4c39cad347668045dfff47b1095cf3632649")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

