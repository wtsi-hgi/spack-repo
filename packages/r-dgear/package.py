# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgear(RPackage):
	"""Differential Gene Expression Analysis with R

	Analyses gene expression data derived from experiments to detect differentially expressed genes by employing the concept of majority voting with five different statistical models. It includes functions for differential expression analysis, significance testing, etc. It simplifies the process of uncovering meaningful patterns and trends within gene expression data, aiding researchers in downstream analysis. Boyer, R.S., Moore, J.S. (1991) <doi:10.1007/978-94-011-3488-0_5>.
	"""
	
	cran = "DGEAR" 

	version("0.1.3", md5="a6a46a7deabbc37fcced0eeabb16e812")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
