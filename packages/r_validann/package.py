# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValidann(RPackage):
	"""Validation Tools for Artificial Neural Networks

	Methods and tools for analysing and validating the outputs
    and modelled functions of artificial neural networks (ANNs) in terms
    of predictive, replicative and structural validity. Also provides a
    method for fitting feed-forward ANNs with a single hidden layer.
	"""
	
	homepage = "http://github.com/gbhumphrey1/validann"
	cran = "validann" 

	version("1.2.1", md5="a3f07b79de8dcadc03ab66d98906de90")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
