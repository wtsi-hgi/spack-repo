# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMobilityindexr(RPackage):
	"""Calculates Transition Matrices and Mobility Indices

	Measures mobility in a population through transition matrices and mobility indices. Relative, mixed, and absolute transition matrices are supported. The Prais-Bibby, Absolute Movement, Origin Specific, and Weighted Group Mobility indices are supported. Example income and grade data are included.
	"""
	
	cran = "mobilityIndexR" 

	version("0.2.1", md5="56f20a3314653f914b65b51a4b54588a")

	depends_on("r@2.10:", type=("build", "run"))
