# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkmyassignment(RPackage):
	"""Automatic Marking of R Assignments

	Automatic marking of R assignments for students and teachers based
    on 'testthat' test suites.
	"""
	
	cran = "markmyassignment" 

	version("0.8.8", md5="a8a4de79093a95c7dc9b64cbad652050")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-testthat@2:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-checkmate@1:", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
