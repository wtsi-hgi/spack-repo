# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHflights(RPackage):
	"""Flights that departed Houston in 2011

	A data only package containing commercial domestic flights that
    departed Houston (IAH and HOU) in 2011.
	"""
	
	cran = "hflights" 

	version("0.1", md5="8049855f805abe23c84aaa1818ab25a3")

	depends_on("r@2.10:", type=("build", "run"))
