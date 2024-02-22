# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNakagami(RPackage):
	"""Functions for the Nakagami Distribution

	Density, distribution function, quantile function and random 
    generation for the Nakagami distribution of Nakagami (1960) 
    <doi:10.1016/B978-0-08-009306-2.50005-4>.
	"""
	
	homepage = "https://github.com/JonasMoss/nakagami"
	cran = "nakagami" 

	version("1.1.0", md5="bb15cf138e2931866fe5f0b2fa0a08ed")

	depends_on("r-assertthat", type=("build", "run"))
