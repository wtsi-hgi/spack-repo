# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUmpire(RPackage):
	"""Simulating Realistic Gene Expression and Clinical Data

	The Ultimate Microrray Prediction, Reality and Inference
  Engine (UMPIRE) is a package to facilitate the simulation of realistic
  microarray data sets with links to associated outcomes. See Zhang and
  Coombes (2012) <doi:10.1186/1471-2105-13-S13-S1>. Version 2.0 adds the
  ability to simulate realistic mixed-typed clinical data.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "Umpire" 

	version("2.0.10", md5="653cf08ea1cb47c15c7a9f65fa5eaddd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
	depends_on("r-bimodalindex", type=("build", "run"))
