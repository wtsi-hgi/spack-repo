# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBroman(RPackage):
	"""Karl Broman's R Code

	Miscellaneous R functions, including functions related to
    graphics (mostly for base graphics), permutation tests, running
    mean/median, and general utilities.
	"""
	
	homepage = "https://github.com/kbroman/broman"
	cran = "broman" 

	version("0.80", md5="2a785731aad1835f129257f980b9a0ff")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
