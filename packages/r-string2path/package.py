# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RString2path(RPackage):
	"""Rendering Font into 'data.frame'

	Extract glyph information from font data, and translate the
    outline curves to flattened paths or tessellated polygons. The converted
    data is returned as a 'data.frame' in easy-to-plot format.
	"""
	
	homepage = "https://yutannihilation.github.io/string2path/"
	cran = "string2path" 

	version("0.1.6", md5="d6a31d07f21b3a5147d16ff4279ff0d8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
