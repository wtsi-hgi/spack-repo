# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfmeta(RPackage):
	"""Meta-Analysis of Phase I Dose-Finding Early Clinical Trials

	Meta-analysis approaches for Phase I dose finding early phases clinical trials in order to better suit requirements in terms of maximum tolerated dose (MTD) and maximal dose regimen (MDR). This package has currently three different approaches: (a) an approach proposed by Zohar et al, 2011, <doi:10.1002/sim.4121> (denoted as ZKO), (b) the Variance Weighted pooling analysis (called VarWT) and (c) the Random Effects Model Based (REMB) algorithm, where user can input his/her own model based approach or use the existing random effect logistic regression model (named as glimem) through the 'dfmeta' package.
	"""
	
	homepage = "http://github.com/artemis-toumazi/dfmeta"
	cran = "dfmeta" 

	version("1.0.0", md5="ca3afc21e2dae20d458fc45f40e4d52e")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
