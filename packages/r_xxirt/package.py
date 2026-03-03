# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXxirt(RPackage):
	"""Item Response Theory and Computer-Based Testing in R

	A suite of psychometric analysis tools for research and operation, including:
    (1) computation of probability, information, and likelihood for the 3PL, GPCM, and GRM;
    (2) parameter estimation using joint or marginal likelihood estimation method;
    (3) simulation of computerized adaptive testing using built-in or customized algorithms;
    (4) assembly and simulation of multistage testing. 
    The full documentation and tutorials are at <https://github.com/xluo11/xxIRT>.
	"""
	
	homepage = "https://github.com/xluo11/xxIRT"
	cran = "xxIRT" 

	version("2.1.2", md5="1c04517589813b32185da355d4eb53c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glpkapi", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
