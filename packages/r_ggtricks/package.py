# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtricks(RPackage):
	"""Create Sector and Other Charts Easily Using Grammar of Graphics

	A collection of several geoms to create graphics, using
    'ggplot2' and the Cartesian coordinate system. You use the familiar
    mapping 'Grammar of Graphics' without the need to do another
    transformation into polar coordinates.
	"""
	
	homepage = "https://github.com/AbdoulMa/ggtricks"
	cran = "ggtricks" 

	version("0.1.0", md5="64c87791d40522db5d97203e78b72589")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
