# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRttf2pt1(RPackage):
	"""'ttf2pt1' Program

	Contains the program 'ttf2pt1', for use with the
    'extrafont' package. This product includes software developed by the 'TTF2PT1'
    Project and its contributors.
	"""
	
	homepage = "https://github.com/wch/Rttf2pt1"
	cran = "Rttf2pt1" 

	version("1.3.12", md5="993029fbdbaeb22d5b20368d071a1dcd", url="https://cran.r-project.org/src/contrib/Rttf2pt1_1.3.12.tar.gz")

	depends_on("r@2.15:", type=("build", "run"))
