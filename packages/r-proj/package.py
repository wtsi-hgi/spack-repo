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
	version("0.4.0", sha256="dde90cfeca83864e61a7422e1573d2d55bb0377c32b9a8f550f47b8631121ce7")
	version("0.1.0", sha256="5186f221335e8092bbcd4d82bd323ee7e752c7c9cf83d3f94e4567e0b407aa6f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("proj@6.3.1:", type=("build", "link", "run"))
