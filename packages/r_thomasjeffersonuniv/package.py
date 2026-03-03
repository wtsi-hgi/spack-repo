# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThomasjeffersonuniv(RPackage):
	"""Handy Tools for TJU/TJUH Employees

	Functions for admin needs of employees of Thomas Jefferson
        University and Thomas Jefferson University Hospital, Philadelphia,
        PA.
	"""
	
	cran = "ThomasJeffersonUniv" 

	version("0.1.0", md5="2fd64845242f76fe499475601eef49be")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
