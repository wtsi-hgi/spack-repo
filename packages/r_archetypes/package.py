# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchetypes(RPackage):
	"""Archetypal Analysis

	The main function archetypes implements a
    framework for archetypal analysis supporting arbitrary
    problem solving mechanisms for the different conceptual
    parts of the algorithm.
	"""
	
	cran = "archetypes" 

	version("2.2-0.1", md5="e0b69fbd2752d6c41858dfb1a1754fe4")

	depends_on("r-modeltools", type=("build", "run"))
	depends_on("r-nnls@1.1:", type=("build", "run"))
