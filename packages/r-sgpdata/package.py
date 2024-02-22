# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgpdata(RPackage):
	"""Exemplar Data Sets for Student Growth Percentiles (SGP) Analyses

	Data sets utilized by the 'SGP' package as exemplars for users to conduct their own student growth percentiles (SGP) analyses.
	"""
	
	homepage = "https://CenterForAssessment.github.io/SGPdata/"
	cran = "SGPdata" 

	version("27.0-0.0", md5="d0ae550c7e0a8c7aa725ce1c8d7c47e4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
