# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGandatamodel(RPackage):
	"""Build a Metric Subspaces Data Model for a Data Source

	Neural networks are applied to create a density value function which approximates density values for a data source. The trained neural network is analyzed for different levels. For each level metric subspaces with density values above a level are determined. The obtained set of metric subspaces and the trained neural network are assembled into a data model. A prerequisite is the definition of a data source, the generation of generative data and the calculation of density values. These tasks are executed using package 'ganGenerativeData' <https://cran.r-project.org/package=ganGenerativeData>.
	"""
	
	cran = "ganDataModel" 

	version("1.1.6", md5="27df21d94b2d78569fc31b0a75121d02")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tensorflow@2:", type=("build", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
