# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsme(RPackage):
	"""Functions and Datasets for "Methods of Statistical Model
Estimation"

	Functions and datasets from Hilbe, J.M., and Robinson, A.P. 2013. Methods of Statistical Model Estimation. Chapman & Hall / CRC.
	"""
	
	cran = "msme" 

	version("0.5.3", md5="48ab9dfa0200ca7128990c3257f54499")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
