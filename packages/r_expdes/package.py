# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpdes(RPackage):
	"""Experimental Designs Package

	Package for analysis of simple experimental designs (CRD, RBD and LSD), experiments in double factorial schemes (in CRD and RBD), experiments in a split plot in time schemes (in CRD and RBD), experiments in double factorial schemes with an additional treatment (in CRD and RBD), experiments in triple factorial scheme (in CRD and RBD) and experiments in triple factorial schemes with an additional treatment (in CRD and RBD), performing the analysis of variance and means comparison by fitting regression models until the third power (quantitative treatments) or by a multiple comparison test, Tukey test, test  of Student-Newman-Keuls (SNK), Scott-Knott, Duncan test, t test (LSD) and Bonferroni t test (protected LSD) - for qualitative treatments; residual analysis (Ferreira, Cavalcanti and Nogueira, 2014) <doi:10.4236/am.2014.519280>.
	"""
	
	cran = "ExpDes" 

	version("1.2.2", md5="6b2d6b0c72814668ea366aef5f77a828")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stargazer", type=("build", "run"))
