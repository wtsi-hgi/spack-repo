# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgeomstats(RPackage):
	"""Interface to 'Geomstats'

	Provides an interface to the Python package 'Geomstats' authored by Miolane et 
    al. (2020) <arXiv:2004.04667>.
	"""
	
	homepage = "https://github.com/LMJL-Alea/rgeomstats"
	cran = "rgeomstats" 

	version("0.0.1", md5="f2a4ff126b6c59a0551c3b05a659d1e4")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
