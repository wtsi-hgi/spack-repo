# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeoweightedmodel(RPackage):
	"""User-Friendly Interface for Geographically-Weighted Models

	Contains the development of a tool that provides a web-based
    graphical user interface (GUI) to perform Techniques from a subset of
    spatial statistics known as geographically weighted (GW) models.
    Contains methods described by Brunsdon et al., 1996
    <doi:10.1111/j.1538-4632.1996.tb00936.x>, Brunsdon et al., 2002
    <doi:10.1016/s0198-9715(01)00009-6>, Harris et al., 2011
    <doi:10.1080/13658816.2011.554838>, Brunsdon et al., 2007
    <doi:10.1111/j.1538-4632.2007.00709.x>.
	"""
	
	cran = "GeoWeightedModel" 

	version("1.0.3", md5="b95f892227654fe8edbb5bc695fe8fc4")

	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-cartography", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-gwmodel", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
