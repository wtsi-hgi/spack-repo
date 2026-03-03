# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSciviews(RPackage):
	"""SciViews - Main package

	Functions to install SciViews additions to R, and more
        tools.
	"""
	
	homepage = "https://github.com/SciViews/SciViews"
	cran = "SciViews" 

	version("0.9-13.1", md5="05cae4ad06d935b6f0905856563f6854")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
