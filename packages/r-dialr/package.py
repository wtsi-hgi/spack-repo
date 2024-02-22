# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDialr(RPackage):
	"""Parse, Format, and Validate International Phone Numbers

	Parse, format, and validate international phone
    numbers using Google's 'libphonenumber' java library,
    <https://github.com/google/libphonenumber>.
	"""
	
	homepage = "https://socialresearchcentre.github.io/dialr/"
	cran = "dialr" 

	version("0.4.2", md5="e7b7f85a401de3d3dd1266ee3cec15eb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dialrjars@8.10.11.1:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
