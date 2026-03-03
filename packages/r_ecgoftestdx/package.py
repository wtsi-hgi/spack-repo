# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcgoftestdx(RPackage):
	"""A Goodness-of-Fit Test for Elliptical Distributions with
Diagnostic Capabilities

	A goodness-of-fit test for elliptical distributions with diagnostic
  capabilities. Gilles R. Ducharme, Pierre Lafaye de Micheaux (2019) <arXiv:1902.03622>.
	"""
	
	cran = "ECGofTestDx" 

	version("0.4", md5="7ff3e3bdcc3829b508ac52b02bdf8d4b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
