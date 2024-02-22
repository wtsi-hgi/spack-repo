# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernelfactory(RPackage):
	"""Kernel Factory: An Ensemble of Kernel Machines

	Binary classification based on an ensemble of kernel machines ("Ballings, M. and Van den Poel, D. (2013), Kernel Factory: An Ensemble of Kernel Machines. Expert Systems With Applications, 40(8), 2904-2913"). Kernel factory is an ensemble method where each base classifier (random forest) is fit on the kernel matrix of a subset of the training data.
	"""
	
	cran = "kernelFactory" 

	version("0.3.0", md5="479ef6569da2090cc7e2a32e6a838717")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-auc", type=("build", "run"))
	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
