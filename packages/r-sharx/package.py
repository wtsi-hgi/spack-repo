# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharx(RPackage):
	"""Models and Data Sets for the Study of Species-Area Relationships

	Hierarchical models for the analysis of species-area 
  relationships (SARs) by combining several data sets and covariates; 
  with a global data set combining individual SAR studies; 
  as described in Solymos and Lele 
  (2012, Global Ecology and Biogeography 21, 109-120).
	"""
	
	homepage = "https://github.com/psolymos/sharx"
	cran = "sharx" 

	version("1.0-5", md5="c31fe93624dbfd5c02c416e6749a6584")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-dcmle", type=("build", "run"))
	depends_on("r-dclone", type=("build", "run"))
	depends_on("jags@1.0.3:", type=("build", "link", "run"))
