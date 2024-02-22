# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogregequiv(RPackage):
	"""Logistic Regression Equivalence

	Tools for assessing equivalence of similar Logistic Regression models.
	"""
	
	cran = "LogRegEquiv" 

	version("0.1.5", md5="809764328fce5203819de690f7f860d2")

	depends_on("r@2.10:", type=("build", "run"))
