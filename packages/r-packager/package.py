# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackager(RPackage):
	"""Create, Build and Maintain Packages

	Helper functions for package creation, building and
    maintenance. Designed to work with a build system such as 'GNU make' or
    package 'fakemake' to help you to conditionally work through the stages of
    package development (such as spell checking, linting, testing, before
    building and checking a package).
	"""
	
	homepage = "https://gitlab.com/fvafrcu/packager"
	cran = "packager" 

	version("1.15.2", md5="7592620f96169e101d4e9482b04961c6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cyclocomp", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-fakemake@1.10.1:", type=("build", "run"))
	depends_on("r-fritools@3.4:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-rcmdcheck", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-rhub", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-tinytest", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-whoami", type=("build", "run"))
