# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnacor(RPackage):
	"""Simple and Canonical Correspondence Analysis

	Performs simple and canonical CA (covariates on rows/columns) on a two-way frequency table (with missings) by means of SVD. Different scaling methods (standard, centroid, Benzecri, Goodman) as well as various plots including confidence ellipsoids are provided. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/psychor/"
	cran = "anacor" 

	version("1.1-4", md5="41ed0963eeebdf27314cbe31eed16f11")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
