# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoxyglobals(RPackage):
	"""'Roxygen2' Global Variable Declarations

	Generate utils::globalVariables() from 'roxygen2' @global and @autoglobal tags.
	"""
	
	homepage = "https://github.com/anthonynorth/roxyglobals"
	cran = "roxyglobals" 

	version("1.0.0", md5="48733bff6694e5e0b59e5d4d393e4c2a")

	depends_on("r-brio", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
