# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreeze(RPackage):
	"""Functions for Wind Resource Assessment

	A collection of functions to analyse, visualize and interpret wind data
         and to calculate the potential energy production of wind turbines.
	"""
	
	homepage = "https://github.com/chgrl/bReeze"
	cran = "bReeze" 

	version("0.4-4", md5="9d32f6e115ed50b6ed3f45ced635343d")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
