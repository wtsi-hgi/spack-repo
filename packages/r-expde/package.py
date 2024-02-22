# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpde(RPackage):
	"""Modular Differential Evolution for Experimenting with Operators

	Modular implementation of the Differential Evolution algorithm for
    experimenting with different types of operators.
	"""
	
	homepage = "http://github.com/fcampelo/ExpDE"
	cran = "ExpDE" 

	version("0.1.4", md5="35e8d9f73a9115bc7dfff429a065c256")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
