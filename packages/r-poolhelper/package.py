# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoolhelper(RPackage):
	"""Simulates Pooled Sequencing Genetic Data

	Simulates pooled sequencing data under a variety of conditions. 
    Also allows for the evaluation of the average absolute difference between allele frequencies 
    computed from genotypes and those computed from pooled data. 
    Carvalho et al., (2022) <doi:10.1101/2023.01.20.524733>.
	"""
	
	homepage = "https://github.com/joao-mcarvalho/poolHelper"
	cran = "poolHelper" 

	version("1.1.0", md5="da2a9d5f10ac3209dfca06ff5893c387")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-scrm", type=("build", "run"))
