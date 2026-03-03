# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPointdensityp(RPackage):
	"""Point Density for Geospatial Data

	The function pointdensity returns a density count and the temporal average for
    every point in the original list. The dataframe returned includes four
    columns: lat, lon, count, and date_avg. The "lat" column is the original
    latitude data; the "lon" column is the original longitude data; the "count"
    is the density count of the number of points within a radius of
    radius*grid_size (the neighborhood); and the date_avg column includes the
    average date of each point in the neighborhood.
	"""
	
	cran = "pointdensityP" 

	version("0.3.5", md5="0d3f0c76e7c4b1eb4bf60c4212c52644")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
