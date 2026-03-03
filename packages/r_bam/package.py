# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBam(RPackage):
	"""Functions and Datasets for "Bayesian Methods: A Social and
Behavioral Sciences Approach"

	Functions and datasets for Jeff Gill: "Bayesian Methods: A Social and Behavioral Sciences Approach". First, Second, and Third Edition. Published by Chapman and Hall/CRC (2002, 2007, 2014) <doi:10.1201/b17888>.
	"""
	
	cran = "BaM" 

	version("1.0.3", md5="91c36774bf6e725769368260544110c9")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
