# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPixarfilms(RPackage):
	"""Pixar Films and Achievements

	Data about Disney Pixar films provided by Wikipedia. This
    package contains data about the films, the people involved, and their
    awards.
	"""
	
	homepage = "https://github.com/erictleung/pixarfilms"
	cran = "pixarfilms" 

	version("0.2.1", md5="85a42ad7dc854688ed09a636839201b7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
