# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkat(RPackage):
	"""SNP-Set (Sequence) Kernel Association Test

	Functions for kernel-regression-based association tests including Burden test, SKAT and SKAT-O. These methods aggregate individual SNP score statistics in a SNP set and efficiently compute SNP-set level p-values.
	"""
	
	cran = "SKAT" 

	version("2.2.5", md5="1eeba626224438128a4d8b3d5e070c79")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spatest", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
