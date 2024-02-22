# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPspmanalysis(RPackage):
	"""Analysis of Physiologically Structured Population Models

	Performs demographic, bifurcation and evolutionary analysis of physiologically structured population models, which is a class of models that consistently translates continuous-time models of individual life history to the population level.
    A model of individual life history has to be implemented specifying the individual-level functions that determine the life history, such as development and mortality rates and fecundity. 
    M.A. Kirkilionis, O. Diekmann, B. Lisser, M. Nool, B. Sommeijer & A.M. de Roos (2001) <doi:10.1142/S0218202501001264>.
    O.Diekmann, M.Gyllenberg & J.A.J.Metz (2003) <doi:10.1016/S0040-5809(02)00058-8>.
    A.M. de Roos (2008) <doi:10.1111/j.1461-0248.2007.01121.x>.
	"""
	
	cran = "PSPManalysis" 

	version("0.3.9", md5="4c6d407ca52cac8146627f6a9002fd5a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.11:", type=("build", "run"))
	depends_on("r-pkgbuild@1.1:", type=("build", "run"))
