# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfcanalysis(RPackage):
	"""Tools for Working with Hansen et al. Global Forest Change
Dataset

	Supports analyses using the Global Forest Change dataset released
    by Hansen et al. gfcanalysis was originally written for the Tropical Ecology 
    Assessment and Monitoring (TEAM) Network. For additional details on the 
    Global Forest Change dataset, see: Hansen, M. et al. 2013. "High-Resolution 
    Global Maps of 21st-Century Forest Cover Change." Science 342 (15 
    November): 850-53. The forest change data and more information on the 
    product is available at <http://earthenginepartners.appspot.com>.
	"""
	
	homepage = "https://github.com/azvoleff/gfcanalysis"
	cran = "gfcanalysis" 

	version("1.8.0", md5="087a0284f9f05fa83772a38af3dbe8f7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))
