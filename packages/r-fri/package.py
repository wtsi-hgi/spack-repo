# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFri(RPackage):
	"""Relative Importance of Main and Interaction Effects

	Computes relative importance of main and interaction effects. Also, sum of the modified generalized weights is computed. Ibrahim et al. (2022) <doi:10.1134/S1064229322080051>.
	"""
	
	cran = "FRI" 

	version("1.0", md5="a68ece83575e92e77a37037fc6aee8c1")

	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-rsnns", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
