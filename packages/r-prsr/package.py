# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrsr(RPackage):
	"""Test of Periodicity using Response Surface Regression

	Tests periodicity in short time series using response surface regression.
	"""
	
	cran = "pRSR" 

	version("3.1.1", md5="1db67f52bc05de762a226cfc4c9e8a7b")

	depends_on("r@2.10:", type=("build", "run"))
