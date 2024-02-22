# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeofd(RPackage):
	"""Spatial Prediction for Function Value Data

	Kriging based methods are used for predicting functional data 
             (curves) with spatial dependence.
	"""
	
	cran = "geofd" 

	version("2.0", md5="726ca1ac3a08aea3523c7d08bb8d9cef")

	depends_on("r-fda", type=("build", "run"))
