# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShadowtext(RPackage):
	"""Shadow Text Grob and Layer.

	Implement shadowtextGrob() for 'grid' and geom_shadowtext() layer for
	'ggplot2'. These functions create/draw text grob with background shadow."""

	cran = "shadowtext"

	version("0.1.3", md5="7144d2b78c162850634a874e956da1fc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
