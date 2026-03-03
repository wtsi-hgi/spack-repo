# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenocamr(RPackage):
	"""Facilitates 'PhenoCam' Data Access and Time Series
Post-Processing

	
    Programmatic interface to the 'PhenoCam' web services (<https://phenocam.nau.edu/webcam>).
    Allows for easy downloading of 'PhenoCam' data directly to your R workspace
    or your computer and provides post-processing routines for consistent and easy
    timeseries outlier detection, smoothing and estimation of phenological transition dates.
    Methods for this package are described in detail in Hufkens et. al (2018) <doi:10.1111/2041-210X.12970>.
	"""
	
	homepage = "https://github.com/bluegreen-labs/phenocamr"
	cran = "phenocamr" 

	version("1.1.5", md5="4bc767f8ce9f8cc612e421e33d94e816")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-daymetr", type=("build", "run"))
	depends_on("r-modistools", type=("build", "run"))
