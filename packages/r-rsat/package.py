# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsat(RPackage):
	"""Dealing with Multiplatform Satellite Images

	Downloading, customizing, and processing time series of satellite images for a region of interest. 'rsat' functions allow a unified access to multispectral images from Landsat, MODIS and Sentinel repositories. 'rsat' also offers capabilities for customizing satellite images, such as tile mosaicking, image cropping and new variables computation. Finally, 'rsat' covers the processing, including cloud masking, compositing and gap-filling/smoothing time series of images (Militino et al., 2018 <doi:10.3390/rs10030398> and Militino et al., 2019 <doi:10.1109/TGRS.2019.2904193>).
	"""
	
	homepage = "https://github.com/ropensci/rsat"
	cran = "rsat" 

	version("0.1.21", md5="a46d3e29447e2cfb320cecfc31147bec")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-leafem", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-calendr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
