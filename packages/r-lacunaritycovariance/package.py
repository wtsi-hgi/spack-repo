# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLacunaritycovariance(RPackage):
	"""Gliding Box Lacunarity and Other Metrics for 2D Random Closed
Sets

	Functions for estimating the gliding box lacunarity (GBL),
    covariance, and pair-correlation of a random closed set (RACS) in 2D
    from a binary coverage map (e.g. presence-absence land cover maps).
    Contains a number of newly-developed covariance-based estimators of
    GBL (Hingee et al., 2019) <doi:10.1007/s13253-019-00351-9> and
    balanced estimators, proposed by Picka (2000)
    <http://www.jstor.org/stable/1428408>, for covariance, centred
    covariance, and pair-correlation.  Also contains methods for
    estimating contagion-like properties of RACS and simulating 2D Boolean
    models.  Binary coverage maps are usually represented as raster images
    with pixel values of TRUE, FALSE or NA, with NA representing
    unobserved pixels.  A demo for extracting such a binary map from a
    geospatial data format is provided.  Binary maps may also be
    represented using polygonal sets as the foreground, however for most
    computations such maps are converted into raster images.  The package
    is based on research conducted during the author's PhD studies.
	"""
	
	homepage = "https://github.com/kasselhingee/lacunaritycovariance"
	cran = "lacunaritycovariance" 

	version("1.1-7", md5="e6b91edb4ba0d82ba639cf216d9a4b63")

	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-spatstat-explore@3.0.3:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
