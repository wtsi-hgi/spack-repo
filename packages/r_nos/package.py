# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNos(RPackage):
	"""Compute Node Overlap and Segregation in Ecological Networks

	Calculate NOS (node overlap and segregation) and
    the associated metrics described in Strona and Veech (2015)
    <doi:10.1111/2041-210X.12395> and Strona et al. (2018) 
    <doi:10.1111/ecog.03447>. The functions provided in the 
    package enable assessment of structural patterns ranging from
    complete node segregation to perfect nestedness in a variety 
    of network types. In addition, they provide a measure of 
    network modularity.  
	"""
	
	homepage = "https://github.com/txm676/nos"
	cran = "nos" 

	version("2.0.0", md5="61e4c2550b9b74906d044b0a465d402e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
