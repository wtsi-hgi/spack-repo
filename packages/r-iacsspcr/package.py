# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIacsspcr(RPackage):
	"""Data and Functions for "An Intro. to Accept. Samp. & SPC/R"

	Contains data frames and functions used in the book "An Introduction to Acceptance Sampling and SPC with R". This book is available electronically at <https://bookdown.org/>. A physical copy will be published by CRC Press.
	"""
	
	cran = "IAcsSPCR" 

	version("1.2.1", md5="1c31103aad60f3e845d0ccd918788413")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-frf2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
