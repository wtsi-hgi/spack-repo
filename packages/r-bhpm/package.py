# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhpm(RPackage):
	"""Bayesian Hierarchical Poisson Models for Multiple Grouped
Outcomes with Clustering

	Bayesian hierarchical methods for the detection of differences in rates of related outcomes for multiple treatments for clustered observations. Theoretical background for the models is given in Carragher (2017) <https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.736866>. The models in this package are extensions for multiple treatments and clusters. This software was developed for the Precision Drug Theraputics: Risk Prediction in Pharmacoepidemiology project as part of a Rutherford Fund Fellowship at Health Data Research (UK), Medical Research Council (UK) award reference MR/S003967/1 (<https://gtr.ukri.org/>). Principal Investigator: Raymond Carragher.
	"""
	
	cran = "bhpm" 

	version("1.7", md5="6248d8ef160378a2589bbbde8843bb8a")

	depends_on("r-coda", type=("build", "run"))
