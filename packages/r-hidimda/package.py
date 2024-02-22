# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHidimda(RPackage):
	"""High Dimensional Discriminant Analysis

	Performs linear discriminant analysis in high dimensional
        problems based on reliable covariance estimators for problems
        with (many) more variables than observations. Includes routines
        for classifier training, prediction, cross-validation and
        variable selection.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "HiDimDA" 

	version("0.2-4", md5="3b43794dbc0f3b79de77488553ab4999")

	depends_on("r@2.10:", type=("build", "run"))
