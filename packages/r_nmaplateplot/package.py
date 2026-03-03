# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmaplateplot(RPackage):
	"""The Plate Plot for Network Meta-Analysis Results

	A graphical display of results from network meta-analysis (NMA). 
  It is suitable for outcomes like odds ratio (OR), risk ratio (RR), 
  risk difference (RD) and standardized mean difference (SMD). 
  It also has an option to visually display and compare 
  the surface under the cumulative ranking (SUCRA) of different treatments.
	"""
	
	cran = "nmaplateplot" 

	version("1.0.1", md5="ab6b24d9c568f8e26a3ebda847960b07")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
