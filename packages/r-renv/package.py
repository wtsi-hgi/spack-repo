# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRenv(RPackage):
	"""Project Environments for R packages.

	A dependency management toolkit for R. Using 'renv', you can create and
	manage project-local R libraries, save the state of these libraries to a
	'lockfile', and later restore your library as required. Together, these
	tools can help make your projects more isolated, portable, and
	reproducible."""

	cran = "renv"

	version("1.0.3", md5="0a136b5a728fb43098d212a92a0e2b26")

