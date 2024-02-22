# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommonjavajars(RPackage):
	"""Useful Libraries for Building a Java Based GUI under R

	Useful libraries for building a Java based GUI under R are provided.
	"""
	
	homepage = "http://gsrmtp.r-forge.r-project.org/"
	cran = "CommonJavaJars" 

	version("1.0-6", md5="3df6a68c38b87c36541db20fa71b418d")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
