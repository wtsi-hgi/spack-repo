# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirichletreg(RPackage):
	"""Dirichlet Regression

	Implements Dirichlet regression models.
	"""
	
	homepage = "https://github.com/maiermarco/DirichletReg"
	cran = "DirichletReg" 

	version("0.7-1", md5="284ed7f322308f6588e0239190fc95bc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
