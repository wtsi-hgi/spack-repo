# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlasma(RPackage):
	"""Partial LeAst Squares for Multiomic Analysis

	Contains tools for supervised analyses of incomplete, overlapping
  multiomics datasets. Applies partial least squares in multiple steps to find
  models that predict survival outcomes. See Yamaguchi et al. (2023)
  <doi:10.1101/2023.03.10.532096>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "plasma" 

	version("1.0.0", md5="b8eae3601cf7337c640521567830eadd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-plsrcox", type=("build", "run"))
	depends_on("r-polychrome@1.5:", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-beanplot", type=("build", "run"))
	depends_on("r-oompabase", type=("build", "run"))
