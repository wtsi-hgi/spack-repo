# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmadiagt(RPackage):
	"""Network Meta-Analysis of Multiple Diagnostic Tests

	Implements HSROC (hierarchical summary receiver operating characteristic) model developed by Ma, Lian, Chu, Ibrahim, and Chen (2018) <doi:10.1093/biostatistics/kxx025>
  and hierarchical model developed by Lian, Hodges, and Chu (2019) <doi:10.1080/01621459.2018.1476239> for performing meta-analysis for 1-5 diagnostic tests to simultaneously 
    compare multiple tests within a missing data framework. This package evaluates the accuracy of 
    multiple diagnostic tests and also gives graphical representation of the results.
	"""
	
	cran = "NMADiagT" 

	version("0.1.2", md5="3f380002abdd6da10a9e8dbccaa43422")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-imgur", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
