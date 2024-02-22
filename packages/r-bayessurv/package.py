# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayessurv(RPackage):
	"""Bayesian Survival Regression with Flexible Error and Random
Effects Distributions

	Contains Bayesian implementations of the Mixed-Effects Accelerated Failure Time (MEAFT) models
             for censored data. Those can be not only right-censored but also interval-censored,
	     doubly-interval-censored or misclassified interval-censored. The methods implemented in the package
	     have been published in Komárek and Lesaffre (2006, Stat. Modelling) <doi:10.1191/1471082X06st107oa>,
	     Komárek, Lesaffre and Legrand (2007, Stat. in Medicine) <doi:10.1002/sim.3083>, Komárek and Lesaffre (2007, Stat. Sinica) <https://www3.stat.sinica.edu.tw/statistica/oldpdf/A17n27.pdf>, Komárek and Lesaffre (2008, JASA) <doi:10.1198/016214507000000563>,
	     García-Zattera, Jara and Komárek (2016, Biometrics) <doi:10.1111/biom.12424>.	     
	"""
	
	homepage = "https://msekce.karlin.mff.cuni.cz/~komarek/"
	cran = "bayesSurv" 

	version("3.7", md5="82af369a13cf183e4e1badc6dcc5fc17")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-smoothsurv", type=("build", "run"))
