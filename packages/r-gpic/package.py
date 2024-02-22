# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpic(RPackage):
	"""Quantifying Group Performance in Individual Competitions

	Compute the GPIC index as described in Pham (2020)
    <doi:10.35542/osf.io/ajz5v>.
	"""
	
	cran = "GPIC" 

	version("0.1.0", md5="c1efa0ee7e215bf0bc14eaa0671945ed")

	depends_on("r@4:", type=("build", "run"))
