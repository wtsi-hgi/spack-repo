# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgrass(RPackage):
	"""Interface Between 'GRASS' Geographical Information System and
'R'

	An interface between the 'GRASS' geographical information system ('GIS') and 'R', based on starting 'R' from within the 'GRASS' 'GIS' environment, or running a free-standing 'R' session in a temporary 'GRASS' location; the package provides facilities for using all 'GRASS' commands from the 'R' command line. The original interface package for 'GRASS 5' (2000-2010) is described in Bivand (2000) <doi:10.1016/S0098-3004(00)00057-1> and Bivand (2001) <https://www.r-project.org/conferences/DSC-2001/Proceedings/Bivand.pdf>. This was succeeded by 'spgrass6' for 'GRASS 6' (2006-2016) and 'rgrass7' for 'GRASS 7' (2015-present). The 'rgrass' package modernizes the interface for 'GRASS 8' while still permitting the use of 'GRASS 7'.
	"""
	
	homepage = "https://rsbivand.github.io/rgrass/"
	cran = "rgrass" 

	version("0.4-1", md5="e6b4a48b3b776f2d51d28419e2ee8e33")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("grass@7:", type=("build", "link", "run"))
