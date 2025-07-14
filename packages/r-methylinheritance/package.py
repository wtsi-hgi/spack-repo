# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylinheritance(RPackage):
	"""Permutation-Based Analysis associating Conserved Differentially Methylated Elements Across Multiple Generations to a Treatment Effect

	Permutation analysis, based on Monte Carlo sampling, for testing the hypothesis that the number of conserved differentially methylated elements, between several generations, is associated to an effect inherited from a treatment and that stochastic effect can be dismissed.
	"""
	
	homepage = "https://github.com/adeschen/methylInheritance"
	bioc = "methylInheritance"

	version("1.32.0", commit="9a4cf5875bcefa132af30812e8a87a7d7ee5af65")
	version("1.26.0", commit="a5e1dc01e79910846846a2219c23b8dca75b778a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-methylkit", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rebus", type=("build", "run"))
