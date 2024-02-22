# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnockoff(RPackage):
	"""The Knockoff Filter for Controlled Variable Selection

	The knockoff filter is a general procedure for controlling the false discovery rate (FDR)
  when performing variable selection. 
  For more information, see the website below and the accompanying paper: Candes et al., 
  "Panning for gold: model-X knockoffs for high-dimensional controlled variable selection", 
  J. R. Statist. Soc. B (2018) 80, 3, pp. 551-577.
	"""
	
	homepage = "https://web.stanford.edu/group/candes/knockoffs/index.html"
	cran = "knockoff" 

	version("0.3.6", md5="202203a05fa2d3f65266795d63ab47df")

	depends_on("r-rdsdp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
