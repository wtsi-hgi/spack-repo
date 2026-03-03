# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgricolae(RPackage):
	"""Statistical Procedures for Agricultural Research

	Original idea was presented in the thesis "A statistical analysis tool for agricultural research" to obtain the degree of Master on science, National Engineering University (UNI), Lima-Peru. Some experimental data for the examples come from the CIP and others research. Agricolae offers extensive functionality on experimental design especially for agricultural and plant breeding experiments, which can also be useful for other purposes. It supports planning of lattice, Alpha, Cyclic, Complete Block, Latin Square, Graeco-Latin Squares, augmented block, factorial, split and strip plot designs. There are also various analysis facilities for experimental data, e.g. treatment comparison procedures and several non-parametric tests comparison, biodiversity indexes and consensus cluster.
	"""
	
	cran = "agricolae" 

	version("1.3-7", md5="27cdffab9bd7cf428cb005d41db13c00")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-algdesign", type=("build", "run"))
