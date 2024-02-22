# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQueuecomputer(RPackage):
	"""Computationally Efficient Queue Simulation

	Implementation of a computationally efficient method for
    simulating queues with arbitrary arrival and service times. 
    Please see Ebert, Wu, Mengersen & Ruggeri (2020, <doi:10.18637/jss.v095.i05>) 
    for further details. 
	"""
	
	homepage = "https://github.com/AnthonyEbert/queuecomputer"
	cran = "queuecomputer" 

	version("1.2.0", md5="d7643f1ef2dd9ba4677d041eef271235")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.500:", type=("build", "run"))
