# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvglite(RPackage):
	"""An 'SVG' Graphics Device.

	A graphics device for R that produces 'Scalable Vector Graphics'. 'svglite'
	is a fork of the older 'RSvgDevice' package."""

	cran = "svglite"

	license("GPL-2.0-or-later")

	version("2.1.3", md5="46154cf187ad6ec377269b6307de16f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("libpng", type=("build", "link", "run"))
