# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgl(RPackage):
	"""3D Visualization Using OpenGL.

	Provides medium to high level functions for 3D interactive graphics,
	including functions modelled on base graphics (plot3d(), etc.) as well as
	functions for constructing representations of geometric objects (cube3d(),
	etc.). Output may be on screen using OpenGL, or to various standard 3D file
	formats including WebGL, PLY, OBJ, STL as well as 2D image formats,
	including PNG, Postscript, SVG, PGF."""

	cran = "rgl"

	version("1.2.8", md5="781667cf17fdf52609d5b499d7c4af14")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.6:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr@1.33:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.20:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("gl", type=("build", "link", "run"))
	depends_on("glu", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("freetype", type=("build", "link", "run"))

	def configure_args(self):
		args = [
			"--x-includes=%s" % self.spec["libx11"].prefix.include,
			"--x-libraries=%s" % self.spec["libx11"].prefix.lib,
			"--with-gl-includes=%s" % self.spec["gl"].headers.directories[0],
			"--with-gl-libraries=%s" % self.spec["gl"].libs.directories[0],
			"--with-gl-prefix=%s" % self.spec["gl"].home,
		]
		return args
