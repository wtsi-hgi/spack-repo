# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProj4(RPackage):
	"""A simple interface to the PROJ.4 cartographic projections library.

	A simple interface to lat/long projection and datum transformation of the
	PROJ.4 cartographic projections library. It allows transformation of
	geographic coordinates from one projection and/or datum to another."""

	cran = "proj4"

	version("1.0-14", md5="aa4414ed36bacf9c15e3e990b658cd90", url="https://cran.r-project.org/src/contrib/proj4_1.0-14.tar.gz")

	depends_on("r@2:", type=("build", "run"))
	depends_on("proj@4.4.6:", type=("build", "link", "run"))
