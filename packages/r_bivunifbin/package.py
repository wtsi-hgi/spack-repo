# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivunifbin(RPackage):
	"""Generation of Bivariate Uniform Data and Its Relation to
Bivariate Binary Data

	Simulation of bivariate uniform data with a full range of correlations based on 
             two beta densities and computation of the tetrachoric correlation 
             (correlation of bivariate uniform data) from the phi coefficient 
             (correlation of bivariate binary data) and vice versa.
	"""
	
	cran = "BivUnifBin" 

	version("1.3.3", md5="bfcd09b7443a1e4bfe0ba2a7869ebdd8")

	depends_on("r-binordnonnor", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
