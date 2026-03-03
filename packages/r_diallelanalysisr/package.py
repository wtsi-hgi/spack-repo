# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiallelanalysisr(RPackage):
	"""Diallel Analysis with R

	Performs Diallel Analysis with R using Griffing's and Hayman's approaches. Four different Methods (1: Method-I (Parents + F1's + reciprocals); 2: Method-II (Parents and one set of F1's); 3: Method-III (One set of F1's and reciprocals); 4: Method-IV (One set of F1's only)) and two Models (1: Fixed Effects Model; 2: Random Effects Model) can be applied using Griffing's approach.
	"""
	
	homepage = "https://github.com/myaseen208/DiallelAnalysisR"
	cran = "DiallelAnalysisR" 

	version("0.5.0", md5="2ecd7bdc983db323149a1c59fdd6891c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
