# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtheory(RPackage):
	"""Apply Generalizability Theory with R

	Estimates variance components, generalizability coefficients,
    universe scores, and standard errors when observed scores contain variation from
    one or more measurement facets (e.g., items and raters).
	"""
	
	homepage = "http://EvaluationDashboard.com"
	cran = "gtheory" 

	version("0.1.2", md5="9ad4e86a6a77fed1cf618b5c283f60e0")

	depends_on("r-lme4", type=("build", "run"))
