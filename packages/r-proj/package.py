# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProj(RPackage):
	"""Generic Coordinate System Transformations Using 'PROJ'.

	Currently non-operational, a harmless wrapper to allow package 'reproj' to
	install and function while relying on the 'proj4' package."""

	cran = "PROJ"

	version("0.4.5", md5="ee9b558a6519e1a5f6154508a5ea8c11")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("proj@6.3.1:", type=("build", "link", "run"))
