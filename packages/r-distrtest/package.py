# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrtest(RPackage):
	"""Estimation and Testing Classes Based on Package 'distr'

	Evaluation (S4-)classes based on package distr for evaluating procedures
            (estimators/tests) at data/simulation in a unified way.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distrTEst" 

	version("2.8.2", md5="8dd64ed463c4a977ebf42108adb56ae5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-setrng@2006.2.1:", type=("build", "run"))
	depends_on("r-distrsim@2.2:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
