# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwa(RPackage):
	"""Subsampling Winner Algorithm for Classification

	This algorithm conducts variable selection in the classification setting. It repeatedly subsamples variables and runs linear discriminant analysis (LDA) on the subsampled variables. Variables are scored based on the AUC and the t-statistics. Variables then enter a competition and the semi-finalist variables will be evaluated in a final round of LDA classification. The algorithm then outputs a list of variable selected. Qiao, Sun and Fan (2017) <http://people.math.binghamton.edu/qiao/swa.html>.
	"""
	
	cran = "swa" 

	version("0.8.1", md5="11c140cb6887f42e0c091f400d4ba871")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
