# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxnet(RPackage):
	"""Fitting 'Maxent' Species Distribution Models with 'glmnet'

	Procedures to fit species distributions models from occurrence records and environmental variables, using 'glmnet' for model fitting. Model structure is the same as for the 'Maxent' Java package, version 3.4.0, with the same feature types and regularization options.  See the 'Maxent' website <http://biodiversityinformatics.amnh.org/open_source/maxent> for more details.
	"""
	
	homepage = "https://github.com/mrmaxent/maxnet"
	cran = "maxnet" 

	version("0.1.4", md5="8a24d2bdc2a05e384fd3f75b1513c0a6")

	depends_on("r-glmnet", type=("build", "run"))
