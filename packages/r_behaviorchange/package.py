# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBehaviorchange(RPackage):
	"""Tools for Behavior Change Researchers and Professionals

	Contains specialised analyses and
    visualisation tools for behavior change science.
    These facilitate conducting determinant studies
    (for example, using confidence interval-based
    estimation of relevance, CIBER, or CIBERlite
    plots, see Crutzen, Noijen & Peters (2017)
    <doi:10/ghtfz9>),
    systematically developing, reporting,
    and analysing interventions (for example, using
    Acyclic Behavior Change Diagrams), and reporting
    about intervention effectiveness (for example, using
    the Numbers Needed for Change, see Gruijters & Peters
    (2017) <doi:10/jzkt>), and computing the
    required sample size (using the Meaningful Change
    Definition, see Gruijters & Peters (2020)
    <doi:10/ghpnx8>).
    This package is especially useful for
    researchers in the field of behavior change or
    health psychology and to behavior change
    professionals such as intervention developers and
    prevention workers.
	"""
	
	homepage = "https://r-packages.gitlab.io/behaviorchange"
	cran = "behaviorchange" 

	version("0.5.5", md5="a2677673cc65b2533f372456068d959a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biasedurn@1.7:", type=("build", "run"))
	depends_on("r-data-tree@0.7.5:", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-diagrammersvg@0.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-googlesheets4@0.2:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-gtable@0.2:", type=("build", "run"))
	depends_on("r-knitr@1:", type=("build", "run"))
	depends_on("r-rmdpartials@0.5:", type=("build", "run"))
	depends_on("r-ufs@0.3.2:", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
	depends_on("r-yum@0.0.1:", type=("build", "run"))
