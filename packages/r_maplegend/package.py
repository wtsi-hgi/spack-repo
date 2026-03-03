# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaplegend(RPackage):
	"""Legends for Maps

	Create legends for maps and other graphics. Thematic maps need to
    be accompanied by legible legends to be fully comprehensible. This package
    offers a wide range of legends useful for cartography, some of which may
    also be useful for other types of graphics. 
	"""
	
	homepage = "https://github.com/riatelab/maplegend/"
	cran = "maplegend" 

	version("0.1.0", md5="d2ef671e7f6eb50b66317e77c4af887a")

	depends_on("r@3.6:", type=("build", "run"))
