# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpidisplay(RPackage):
	"""Epidemiological Data Display Package

	Package for data exploration and result presentation. Full 'epicalc' package with data management functions is available at '<https://medipe.psu.ac.th/epicalc/>'.
	"""
	
	cran = "epiDisplay" 

	version("3.5.0.2", md5="0f8a1029632cf474f1661330b843c44b")

	depends_on("r@2.6.2:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
