# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgeedim(RPackage):
	"""Search, Composite, and Download 'Google Earth Engine' Imagery
with the 'Python' Module 'geedim'

	Search, composite, and download 'Google Earth Engine' imagery with 'reticulate' bindings for the 'Python' module 'geedim' by Dugal Harris. Read the 'geedim' documentation here: <https://geedim.readthedocs.io/>.
    Wrapper functions are provided to make it more convenient to use 'geedim' to download images larger than the 'Google Earth Engine' size limit <https://developers.google.com/earth-engine/apidocs/ee-image-getdownloadurl>.
    By default the "High Volume" API endpoint <https://developers.google.com/earth-engine/cloud/highvolume> is used to download data and this URL can be customized during initialization of the package.
	"""
	
	homepage = "https://humus.rocks/rgeedim/"
	cran = "rgeedim" 

	version("0.2.7", md5="d69910a54a8bc4a1fbfe5e01ffc65ef6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
