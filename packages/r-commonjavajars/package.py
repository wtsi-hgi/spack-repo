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

	version("1.1-0", md5="74f6c68548cd4af15a44bdd418f536d2")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
