# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeccurvier(RPackage):
	"""Easy, Fast, and Pretty Specification Curve Analysis

	Making specification curve analysis easy, fast, and pretty. It 
  improves upon existing offerings with additional features and 'tidyverse' 
  integration. Users can easily visualize and evaluate how their models behave 
  under different specifications with a high degree of customization. For a 
  description and applications of specification curve analysis see Simonsohn, 
  Simmons, and Nelson (2020) <doi:10.1038/s41562-020-0912-z>.
	"""
	
	homepage = "https://github.com/zaynesember/speccurvieR"
	cran = "speccurvieR" 

	version("0.3.0", md5="52476644091da00a29c1436e5179a423")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
