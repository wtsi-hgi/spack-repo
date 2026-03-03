# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotsemm(RPackage):
	"""Graphing Nonlinear Relations Among Latent Variables from
Structural Equation Mixture Models

	Contains a graphical user interface to generate the diagnostic
    plots proposed by Bauer (2005; <doi:10.1207/s15328007sem1204_1>), 
    Pek & Chalmers (2015; <doi:10.1080/10705511.2014.937790>), and
    Pek, Chalmers, R. Kok, & Losardo (2015; <doi:10.3102/1076998615589129>) to investigate
    nonlinear bivariate relationships in latent regression models using structural
    equation mixture models (SEMMs).
	"""
	
	homepage = "https://github.com/philchalmers/plotSEMM"
	cran = "plotSEMM" 

	version("2.4", md5="1a4fa91db99a18c94f21ebaf6191d161")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
