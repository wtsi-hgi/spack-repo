# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInldata(RPackage):
	"""Collection of Datasets for the USGS-INL Monitoring Networks

	A collection of analysis-ready datasets for the
   U.S. Geological Survey - Idaho National Laboratory (USGS-INL)
   groundwater and surface-water monitoring networks, administered by the
   USGS-INL Project Office in cooperation with the U.S. Department of Energy.
   The data collected from wells and surface-water stations at the
   Idaho National Laboratory and surrounding areas have been used to describe
   the effects of waste disposal on water contained in the
   eastern Snake River Plain aquifer, located in the southeastern part of
   Idaho, and the availability of water for long-term consumptive and
   industrial use. The package includes long-term monitoring records dating
   back to measurements from 1922. Geospatial data describing the areas from
   which samples were collected or observations were made are also included in
   the package. Bundling this data into a single package significantly reduces
   the magnitude of data processing for researchers and provides a way to
   distribute the data along with its documentation in a standard format.
   Geospatial datasets are made available in a common projection and datum, and
   geohydrologic data have been structured to facilitate analysis.
	"""
	
	homepage = "https://code.usgs.gov/inl/inldata"
	cran = "inldata" 

	version("1.1.4", md5="22525c7204611125bfc7130d3f8d86c4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
