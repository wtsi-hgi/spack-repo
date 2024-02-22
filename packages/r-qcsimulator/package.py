# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcsimulator(RPackage):
	"""A 5-Qubit Quantum Computing Simulator

	Simulates a 5 qubit Quantum Computer and evaluates quantum circuits with 1,2
             qubit quantum gates.
	"""
	
	homepage = "https://github.com/tvganesh/QCSimulator"
	cran = "QCSimulator" 

	version("0.0.1", md5="ff8f42c22bf078077d72ba06952d2853")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
