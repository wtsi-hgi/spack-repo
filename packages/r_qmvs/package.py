# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQmvs(RPackage):
	"""Queueing Model of Visual Search

	The queueing model of visual search models the accuracy and response time data in a visual search experiment using queueing models with finite customer population and stopping criteria of completing the service for finite number of customers. It implements the conceptualization of a hybrid model proposed by Moore and Wolfe (2001), in which visual stimuli enter the processing one after the other and then are identified in parallel. This package provides functions that simulate the specified queueing process and calculate the Wasserstein distance between the empirical response times and the model prediction.
	"""
	
	cran = "qmvs" 

	version("0.2.0", md5="a32b6bacf79c150dcf2d226f3075975d")

	depends_on("r@3:", type=("build", "run"))
