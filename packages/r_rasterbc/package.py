# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterbc(RPackage):
	"""Access Forest Ecology Layers for British Columbia in 2001-2018

	R-based access to a large set of data variables relevant to forest ecology in British Columbia (BC), Canada. Layers
    are in raster format at 100m resolution in the BC Albers projection, hosted at the Federated Research Data Repository (FRDR)
    with <doi:10.20383/101.0283>. The collection includes: elevation; biogeoclimatic zone; wildfire; cutblocks; forest attributes from
    Hansen et al. (2013) <doi:10.1139/cjfr-2013-0401> and Beaudoin et al. (2017) <doi:10.1139/cjfr-2017-0184>; and rasterized
    Forest Insect and Disease Survey (FIDS) maps for a number of insect pest species, all covering the period 2001-2018.
    Users supply a polygon or point location in the province of BC, and 'rasterbc' will download the overlapping raster tiles
    hosted at FRDR, merging them as needed and returning the result in R as a 'SpatRaster' object. Metadata associated with these
    layers, and code for downloading them from their original sources can be found in the 'github' repository
    <https://github.com/deankoch/rasterbc_src>.
	"""
	
	homepage = "https://github.com/deankoch/rasterbc"
	cran = "rasterbc" 

	version("1.0.2", md5="44db1420ad17846d3c8f1bc0ecb793f1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
