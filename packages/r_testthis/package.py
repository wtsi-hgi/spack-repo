# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestthis(RPackage):
	"""Utils and 'RStudio' Addins to Make Testing Even More Fun

	Utility functions and 'RStudio' addins for writing,
    running and organizing automated tests. Integrates tightly with the
    packages 'testthat', 'devtools' and 'usethis'.  Hotkeys can be
    assigned to the 'RStudio' addins for running tests in a single file or
    to switch between a source file and the associated test file. In
    addition, testthis provides function to manage and run tests in
    subdirectories of the test/testthat directory.
	"""
	
	homepage = "https://s-fleck.github.io/testthis"
	cran = "testthis" 

	version("1.1.1", md5="832bb1db173b42ed728e2ee984d564be")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-usethis@0.1:", type=("build", "run"))
