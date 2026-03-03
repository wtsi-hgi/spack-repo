# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REchoFind(RPackage):
	"""Finding Rhythms Using Extended Circadian Harmonic Oscillators
(ECHO)

	Provides a function (echo_find()) designed to find rhythms 
    from data using extended harmonic oscillators. For more information,
    see H. De los Santos et al. (2020) <doi:10.1093/bioinformatics/btz617> .
	"""
	
	homepage = "https://github.com/delosh653/ECHO"
	cran = "echo.find" 

	version("4.0.1", md5="6aa949df58f480cca3a716ef3f5d54e9")

	depends_on("r-minpack-lm@1.2.1:", type=("build", "run"))
	depends_on("r-boot@1.3.22:", type=("build", "run"))
