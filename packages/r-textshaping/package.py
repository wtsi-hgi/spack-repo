# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextshaping(RPackage):
	"""Bindings to the 'HarfBuzz' and 'Fribidi' Libraries for Text Shaping.

	Provides access to the text shaping functionality in the 'HarfBuzz' library
	and the bidirectional algorithm in the 'Fribidi' library. 'textshaping' is
	a low-level utility package mainly for graphic devices that expands upon
	the font tool-set provided by the 'systemfonts' package."""

	cran = "textshaping"
	version("0.3.6", sha256="80e2c087962f55ce2811fbc798b09f5638c06c6b28c10cd3cb3827005b902ada")
	version("0.3.7", md5="75e150aec896dd1807e84538456d22e3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-systemfonts@1:", type=("build", "run"))
	depends_on("r-cpp11@0.2.1:", type=("build", "run"))
	depends_on("freetype@2:", type=("build", "link", "run"))
	depends_on("harfbuzz", type=("build", "link", "run"))
	depends_on("fribidi", type=("build", "link", "run"))
