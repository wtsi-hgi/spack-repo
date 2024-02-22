# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAspace(RPackage):
	"""Functions for Estimating Centrographic Statistics

	A collection of functions for computing centrographic
        statistics (e.g., standard distance, standard deviation
        ellipse, standard deviation box) for observations taken at
        point locations. Separate plotting functions have been
        developed for each measure. Users interested in writing results
        to ESRI shapefiles can do so by using results from 'aspace'
        functions as inputs to the convert.to.shapefile() and
        write.shapefile() functions in the 'shapefiles' library. We intend to
        provide 'terra' integration for geographic data in a future release.
        The 'aspace' package was originally conceived to aid in the analysis of
        spatial patterns of travel behaviour (see Buliung and Remmel 2008
        <doi:10.1007/s10109-008-0063-7>).
	"""
	
	cran = "aspace" 

	version("4.1.0", md5="c845088f38ae5b431d493dcf7388e198")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
