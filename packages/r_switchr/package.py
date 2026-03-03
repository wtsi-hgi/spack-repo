# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwitchr(RPackage):
	"""Installing, Managing, and Switching Between Distinct Sets of
Installed Packages

	Provides an abstraction for managing, installing,
    and switching between sets of installed R packages. This allows users to
    maintain multiple package libraries simultaneously, e.g. to maintain
    strict, package-version-specific reproducibility of many analyses, or
    work within a development/production release paradigm. Introduces a
    generalized package installation process which supports multiple repository
    and non-repository sources and tracks package provenance.
	"""
	
	homepage = "https://github.com/gmbecker/switchr"
	cran = "switchr" 

	version("0.14.8", md5="09fc36407ff8bb1e13a8c760ce0a0e1b")

	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("git", type=("build", "link", "run"))
	depends_on("subversion", type=("build", "link", "run"))
