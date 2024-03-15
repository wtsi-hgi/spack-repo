# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFawr(RPackage):
	"""Functions and Datasets for "Forest Analytics with R"

	Provides functions and datasets from the book "Forest Analytics with R".
	"""
	
	cran = "FAwR" 

	version("1.1.2", md5="ba25a78ba999043957205474cf76ed94")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-glpkapi", type=("build", "run"))
