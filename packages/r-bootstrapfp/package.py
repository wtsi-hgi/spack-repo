# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootstrapfp(RPackage):
	"""Bootstrap Algorithms for Finite Population Inference

	Finite Population bootstrap algorithms to estimate the variance
    of the Horvitz-Thompson estimator for single-stage sampling. 
    For a survey of bootstrap methods for finite populations, see Mashreghi et Al. (2016) <doi:10.1214/16-SS113>.
	"""
	
	cran = "bootstrapFP" 

	version("0.4.6", md5="92c3fa8cf2ee51991ff4c83d10da062c")
	version("0.4.5", md5="977e84df69436d39603867b2fad0004b")

	depends_on("r-sampling", type=("build", "run"))
