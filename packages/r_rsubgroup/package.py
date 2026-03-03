# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsubgroup(RPackage):
	"""Subgroup Discovery and Analytics

	A collection of efficient and effective tools and
	algorithms for subgroup discovery and analytics. The package
	integrates an R interface to the org.vikamine.kernel library
	of the VIKAMINE system <http://www.vikamine.org> implementing
	subgroup discovery, pattern mining and analytics in Java.
	"""
	
	homepage = "https://rsubgroup.org"
	cran = "rsubgroup" 

	version("1.1", md5="339d05c7b01125df0c8784474fc28b11")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("r-foreign@0.8.40:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
