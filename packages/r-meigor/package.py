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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MEIGOR_1.36.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MEIGOR/MEIGOR_1.36.2.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.2", sha256="2ba0d0049e4bdf95b0d20be21c41ae45fb801e46d07e83dd915443fdee7d5d26")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-cnorode", type=("build", "run"))
