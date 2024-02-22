# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhonr(RPackage):
	"""Tools for Phoneticians and Phonologists

	Tools for phoneticians and phonologists, including functions for normalization and plotting of vowels.
	"""
	
	homepage = "http://drammock.github.io/phonR/"
	cran = "phonR" 

	version("1.0-7", md5="69bc235fca50222f5478828d075e980a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
