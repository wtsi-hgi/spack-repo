# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApex(RPackage):
	"""Phylogenetic Methods for Multiple Gene Data

	Toolkit for the analysis of multiple gene data (Jombart et al. 2017) <doi:10.1111/1755-0998.12567>. 
    'apex' implements the new S4 classes 'multidna', 'multiphyDat' and associated methods to handle aligned DNA sequences from multiple genes.
	"""
	
	homepage = "https://github.com/thibautjombart/apex"
	cran = "apex" 

	version("1.0.6", md5="7e3230f3462df4149616abf4ba86df29")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
