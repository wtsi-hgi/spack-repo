# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeigor(RPackage):
	"""MEIGOR - MEtaheuristics for bIoinformatics Global Optimization

	MEIGOR provides a comprehensive environment for performing global optimization tasks in bioinformatics and systems biology. It leverages advanced metaheuristic algorithms to efficiently search the solution space and is specifically tailored to handle the complexity and high-dimensionality of biological datasets. This package supports various optimization routines and is integrated with Bioconductor's infrastructure for a seamless analysis workflow.
	"""
	
	bioc = "MEIGOR"

	version("1.42.0", commit="8926aac2ea996152d8457a5b2f2643eda329aee1")
	version("1.36.2", commit="14f8e8196f5d226eedeb6e8b82a3fed926fede22")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-cnorode", type=("build", "run"))
