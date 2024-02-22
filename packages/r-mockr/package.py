# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMockr(RPackage):
	"""Mocking in R

	Provides a means to mock a package function, i.e.,
    temporarily substitute it for testing. Designed as a drop-in
    replacement for the now deprecated 'testthat::with_mock()' and
    'testthat::local_mock()'.
	"""
	
	homepage = "https://krlmlr.github.io/mockr/"
	cran = "mockr" 

	version("0.2.1", md5="64562ef53ff44054bec118181cd72e65")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
