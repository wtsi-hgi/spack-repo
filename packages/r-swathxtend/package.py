# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwathxtend(RPackage):
	"""SWATH extended library generation and statistical data analysis

	Contains utility functions for integrating spectral libraries for SWATH and statistical data analysis for SWATH generated data.
	"""
	
	bioc = "SwathXtend"

	version("2.30.0", commit="157ffd9530d11bb17144dcbd5a52bdbc002b15f2")
	version("2.24.0", commit="7b0e1381d1f0cc295e45a9206144997d0357008b")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
