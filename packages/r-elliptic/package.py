# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElliptic(RPackage):
	"""Weierstrass and Jacobi Elliptic Functions

	
 A suite of elliptic and related functions including Weierstrass and
 Jacobi forms.  Also includes various tools for manipulating and
 visualizing complex functions.
	"""
	
	homepage = "https://github.com/RobinHankin/elliptic.git"
	cran = "elliptic" 

	version("1.4-0", md5="eb083f4e62ee749a5eec9febb353a49f")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
