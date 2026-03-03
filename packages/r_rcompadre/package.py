# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcompadre(RPackage):
	"""Utilities for using the 'COM(P)ADRE' Matrix Model Database

	Utility functions for interacting with the 'COMPADRE' and
    'COMADRE' databases of matrix population models. Described in Jones et
    al. (2021) <doi:10.1101/2021.04.26.441330>.
	"""
	
	homepage = "https://github.com/jonesor/Rcompadre"
	cran = "Rcompadre" 

	version("1.3.0", md5="cde0e3e44768a754ae9d5a94a59e664f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-popdemo", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
