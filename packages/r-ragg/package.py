# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagg(RPackage):
	"""Graphic Devices Based on AGG.

	Anti-Grain Geometry (AGG) is a high-quality and high-performance 2D drawing
	library. The 'ragg' package provides a set of graphic devices based on AGG
	to use as alternative to the raster devices provided through the
	'grDevices' package."""

	cran = "ragg"
	version("1.2.5", sha256="936f4d75e0e01cdeefb9f57d121cdd7812d0de5a9e1a3a8315f92ce1c84da8f9")
	version("1.2.4", sha256="c547e5636a2eefaa0021a0d50fad1e813c2ce976ec0c9c3f796d38a110680dcd")
	version("1.2.3", sha256="976da0007ef0d4dbadda4734727b539671b65c1eff4ff392d734f4e2c846f2b2")
	version("1.3.0", md5="dc546005cff17506bf712be3e7dbf610")

	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-textshaping", type=("build", "run"))
	depends_on("freetype@2:", type=("build", "link", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))
