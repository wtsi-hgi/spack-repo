# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkeletor(RPackage):
	"""An R Package Skeleton Generator

	A tool for bootstrapping new packages with useful defaults,
    including a test suite outline that passes checks and helpers for running
    tests, checking test coverage, building vignettes, and more. Package
    skeletons it creates are set up for pushing your package to
    'GitHub' and using other hosted services for building and test automation.
	"""
	
	homepage = "https://github.com/nealrichardson/skeletor"
	cran = "skeletor" 

	version("1.0.4", md5="d39fb7b4311af1f9247636f6739ad792")

	depends_on("r@3:", type=("build", "run"))
