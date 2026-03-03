# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuarrint(RPackage):
	"""Interaction Prediction Between Groundwater and Quarry Extension
Using Discrete Choice Models and Artificial Neural Networks

	An implementation of two interaction indices between extractive
    activity and groundwater resources based on hazard and vulnerability
    parameters used in the assessment of natural hazards. One index is based
    on a discrete choice model and the other is relying on an artificial
    neural network.
	"""
	
	homepage = "https://github.com/jojo-/quarrint"
	cran = "quarrint" 

	version("1.0.0", md5="eb26f257b243706db5af0ed1df01e046")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
