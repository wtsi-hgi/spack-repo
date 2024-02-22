# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagickgui(RPackage):
	"""GUI Tools for Interactive Image Processing with 'magick'

	Enables us to use the functions of the package 'magick' interactively.
	"""
	
	homepage = "https://github.com/ShotaOchi/magickGUI"
	cran = "magickGUI" 

	version("1.3.1", md5="768edda20abbd66aa1009e61407b9bdb")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-magick@2.2:", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
