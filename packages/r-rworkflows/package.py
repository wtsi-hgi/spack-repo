# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRworkflows(RPackage):
	"""Test, Document, Containerise, and Deploy R Packages

	Reproducibility is essential to the progress of research, 
  yet achieving it remains elusive even in computational fields. 
  Continuous Integration (CI) platforms offer a powerful way to launch automated workflows 
  to check and document code, but often require considerable time, effort, 
  and technical expertise to setup. We therefore developed the rworkflows suite 
  to make robust CI workflows easy and freely accessible to all R package developers. 
  rworkflows consists of 1) a CRAN/Bioconductor-compatible R package template, 
  2) an R package to quickly implement a standardised workflow, and 
  3) a centrally maintained GitHub Action. 
	"""
	
	homepage = "https://github.com/neurogenomics/rworkflows"
	cran = "rworkflows" 

	version("1.0.1", md5="f1848182d5ad6dff7630aea5e73bce18")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-badger", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
