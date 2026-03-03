# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetamer(RPackage):
	"""Create Data with Identical Statistics

	Creates data with identical statistics (metamers) using an iterative 
   algorithm proposed by Matejka & Fitzmaurice (2017) <DOI:10.1145/3025453.3025912>.
	"""
	
	homepage = "https://eliocamp.github.io/metamer/"
	cran = "metamer" 

	version("0.3.0", md5="848d7c9cfd26f0cff172f9f737e32421")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
