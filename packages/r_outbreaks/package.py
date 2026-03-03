# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutbreaks(RPackage):
	"""A Collection of Disease Outbreak Data

	Empirical or simulated disease outbreak data, provided either as
    RData or as text files.
	"""
	
	homepage = "https://github.com/reconhub/outbreaks"
	cran = "outbreaks" 

	version("1.9.0", md5="760a52ef5c8d97ebc7f1eb725a0144fd")

	depends_on("r@3:", type=("build", "run"))
