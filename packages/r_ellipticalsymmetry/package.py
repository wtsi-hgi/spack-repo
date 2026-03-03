# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REllipticalsymmetry(RPackage):
	"""Elliptical Symmetry Tests

	Given the omnipresence of the assumption of elliptical symmetry, it is essential to be able to test whether that assumption actually holds true or not for the data
            at hand. This package provides several statistical tests for elliptical symmetry that are described in Babic et al. (2021) <arXiv:2011.12560v2>.
	"""
	
	cran = "ellipticalsymmetry" 

	version("0.1.2", md5="0d57b8552511c5ff4943b7314ace1183")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-icsnp@1.1.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.16:", type=("build", "run"))
	depends_on("r-dorng@1.8.2:", type=("build", "run"))
