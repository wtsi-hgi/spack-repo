# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQqman(RPackage):
	"""Q-Q and Manhattan Plots for GWAS Data

	Create Q-Q and manhattan plots for GWAS data from PLINK results.
	"""
	
	homepage = "https://github.com/stephenturner/qqman"
	cran = "qqman" 

	version("0.1.9", md5="af41e4fe81ff4b26cd9d69e70c31a8df")
	version("0.1.8", md5="986eb63b634c55c3a08dc3c2091aecd9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
