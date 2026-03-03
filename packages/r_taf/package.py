# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaf(RPackage):
	"""Transparent Assessment Framework for Reproducible Research

	Functions to organize data, methods, and results used in scientific
  analyses. A TAF analysis consists of four scripts (data.R, model.R, output.R,
  report.R) that are run sequentially. Each script starts by reading files from
  a previous step and ends with writing out files for the next step. Convenience
  functions are provided to version control the required data and software, run
  analyses, clean residues from previous runs, manage files, manipulate tables,
  and produce figures. With a focus on stability and reproducible analyses, TAF
  is designed to have no package dependencies. TAF forms a base layer for the
  'icesTAF' package and other scientific applications.
	"""
	
	homepage = "https://github.com/ices-tools-prod/TAF"
	cran = "TAF" 

	version("4.2.0", md5="782030ccee91f7b888a30c8c6f5df080")

	depends_on("r-lattice", type=("build", "run"))
