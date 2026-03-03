# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeyboard(RPackage):
	"""Bayesian Designs for Early Phase Clinical Trials

	We developed a package 'Keyboard' for designing single-agent, drug-combination, or phase I/II dose-finding clinical trials. The 'Keyboard' designs are novel early phase trial designs that can be implemented simply and transparently, similar to the 3+3 design, but yield excellent performance, comparable to those of more-complicated, model-based designs (Yan F, Mandrekar SJ, Yuan Y (2017) <doi:10.1158/1078-0432.CCR-17-0220>, Li DH, Whitmore JB, Guo W, Ji Y. (2017) <doi:10.1158/1078-0432.CCR-16-1125>,  Liu S, Johnson VE (2016) <doi:10.1093/biostatistics/kxv040>, Zhou Y, Lee JJ, Yuan Y (2019) <doi:10.1002/sim.8475>, Pan H, Lin R, Yuan Y (2020) <doi:10.1016/j.cct.2020.105972>). The 'Keyboard' package provides tools for designing, conducting, and analyzing single-agent, drug-combination, and phase I/II dose-finding clinical trials. For more details about how to use this packge, please refer to Li C, Sun H, Cheng C, Tang L, and Pan H. (2022) "A software tool for both the maximum tolerated dose and the optimal biological dose finding trials in early phase designs". Manuscript submitted for publication.
	"""
	
	cran = "Keyboard" 

	version("0.1.3", md5="741844cadbdeff51900f1352d72e8d92")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
