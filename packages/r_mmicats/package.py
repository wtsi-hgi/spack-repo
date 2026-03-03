# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmicats(RPackage):
	"""Cluster Adjusted t Statistic Applications

	Simulation results detailed in Esarey and Menger (2019) <doi:10.1017/psrm.2017.42>
    demonstrate that cluster adjusted t statistics (CATs) are an effective method
    for correcting standard errors in scenarios with a small number of clusters.
    The 'mmiCATs' package offers a suite of tools for working with CATs. The
    mmiCATs() function initiates a 'shiny' web application, facilitating
    the analysis of data utilizing CATs, as implemented in the cluster.im.glm()
    function from the 'clusterSEs' package. Additionally, the pwr_func_lmer()
    function is designed to simplify the process of conducting simulations to
    compare mixed effects models with CATs models. For educational purposes, the
    CloseCATs() function launches a 'shiny' application card game, aimed at enhancing
    users' understanding of the conditions under which CATs should be preferred
    over random intercept models.
	"""
	
	homepage = "https://github.com/mightymetrika/mmiCATs"
	cran = "mmiCATs" 

	version("0.1.1", md5="cd231d74e5ba9f574007dc7e13a0ab9f")

	depends_on("r-broom", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-clusterses", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mmcards", type=("build", "run"))
	depends_on("r-robust", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
