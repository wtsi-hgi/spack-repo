# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterfr(RPackage):
	"""Interference Color Charts for Polarized Light Microscopy

	Computes interference color tables and plots customized Michel-Levy or Raith-Sorensen charts. Automatic interpretation of polarized-light microscopy images is still under development and will come soon.
	"""
	
	cran = "interfr" 

	version("0.1.0", md5="20fc940f1599cbf71a37abac0936bb3a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-colorspec", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
