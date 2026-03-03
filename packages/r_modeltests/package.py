# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeltests(RPackage):
	"""Testing Infrastructure for Broom Model Generics

	Provides a number of testthat tests that can be
    used to verify that tidy(), glance() and augment() methods meet
    consistent specifications. This allows methods for the same generic to
    be spread across multiple packages, since all of those packages can
    make the same guarantees to users about returned objects.
	"""
	
	homepage = "https://github.com/alexpghayes/modeltests"
	cran = "modeltests" 

	version("0.1.5", md5="ad4725c35d14853a164080746157e9d7")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-testthat@2:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
