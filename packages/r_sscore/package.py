# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSscore(RPackage):
	"""S-Score Algorithm for Affymetrix Oligonucleotide Microarrays

	This package contains an implementation of the S-Score algorithm as described by Zhang et al (2002).
	"""
	
	homepage = "http://home.att.net/~richard-kennedy/professional.html"
	bioc = "sscore" 

	version("1.74.0", commit="79bcdaa243e3b740205df9149c06b585f14543ff")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-affyio", type=("build", "run"))
