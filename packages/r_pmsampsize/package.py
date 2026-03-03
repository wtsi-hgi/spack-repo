# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmsampsize(RPackage):
	"""Sample Size for Development of a Prediction Model

	Computes the minimum sample size required for the development of a new multivariable prediction model using the criteria proposed by Riley et al. (2018) <doi: 10.1002/sim.7992>. pmsampsize can be used to calculate the minimum sample size for the development of models with continuous, binary or survival (time-to-event) outcomes. Riley et al. (2018) <doi: 10.1002/sim.7992> lay out a series of criteria the sample size should meet. These aim to minimise the overfitting and to ensure precise estimation of key parameters in the prediction model.
	"""
	
	cran = "pmsampsize" 

	version("1.1.3", md5="5c040c803e34739325d4331ea39f15bb")

	depends_on("r@2.1:", type=("build", "run"))
