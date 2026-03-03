# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGe(RPackage):
	"""General Equilibrium Modeling

	Some tools for developing general equilibrium models and some general equilibrium models. These models can be used for teaching economic theory and are built by the methods of new structural economics (see <https://www.nse.pku.edu.cn/> and LI Wu, 2019, ISBN: 9787521804225, General Equilibrium and Structural Dynamics: Perspectives of New Structural Economics. Beijing: Economic Science Press). The model form and mathematical methods can be traced back to J. von Neumann (1945, A Model of General Economic Equilibrium. The Review of Economic Studies, 13. pp. 1-9), J. G. Kemeny, O. Morgenstern and G. L. Thompson (1956, A Generalization of the von Neumann Model of an Expanding Economy, Econometrica, 24, pp. 115-135) et al. By the way, J. G. Kemeny is a co-inventor of the computer language BASIC.
	"""
	
	cran = "GE" 

	version("0.4.2", md5="bdc1156045dd2f336e008e0cb3321f4a")

	depends_on("r-cge", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
