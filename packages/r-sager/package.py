# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSager(RPackage):
	"""Applied Statistics for Economics and Management with R

	Datasets and functions for the book "Statistiques pour l’économie et la gestion", "Théorie et applications en entreprise", F. Bertrand, Ch. Derquenne, G. Dufrénot, F. Jawadi and M. Maumy, C. Borsenberger editor, (2021, ISBN:9782807319448, De Boeck Supérieur, Louvain-la-Neuve). 
    The first chapter of the book is dedicated to an introduction to statistics and their world. 
    The second chapter deals with univariate exploratory statistics and graphics. 
    The third chapter deals with bivariate and multivariate exploratory statistics and graphics. 
    The fourth chapter is dedicated to data exploration with Principal Component Analysis. 
    The fifth chapter is dedicated to data exploration with Correspondance Analysis.
    The sixth chapter is dedicated to data exploration with Multiple Correspondance Analysis. 
    The seventh chapter is dedicated to data exploration with automatic clustering. 
    The eighth chapter is dedicated to an introduction to probability theory and classical probability distributions.
    The ninth chapter is dedicated to an estimation theory, one-sample and two-sample tests.
    The tenth chapter is dedicated to an Gaussian linear model.
    The eleventh chapter is dedicated to an introduction to time series.
    The twelfth chapter is dedicated to an introduction to probit and logit models.
    Various example datasets are shipped with the package as well as some new functions.
	"""
	
	homepage = "https://fbertran.github.io/homepage/"
	cran = "sageR" 

	version("0.6.1", md5="4e6e73aa14a33bde4a36ebfc7812d9fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
