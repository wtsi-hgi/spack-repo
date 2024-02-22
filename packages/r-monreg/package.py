# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonreg(RPackage):
	"""Nonparametric Monotone Regression

	Estimates monotone regression and variance functions in a nonparametric model, based on Dette, Holger, Neumeyer, and Pilz (2006) <doi:10.3150/bj/1151525131>.
	"""
	
	homepage = "https://gitlab.com/scottkosty/monreg"
	cran = "monreg" 

	version("0.1.4.1", md5="ee0969090ce7d295e4d5c42efaeec146")

	depends_on("r@2:", type=("build", "run"))
