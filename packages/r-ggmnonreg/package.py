# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmnonreg(RPackage):
	"""Non-Regularized Gaussian Graphical Models

	Estimate non-regularized Gaussian graphical models, Ising models, 
  and mixed graphical models. The current methods consist of multiple regression, 
  a non-parametric bootstrap  <doi:10.1080/00273171.2019.1575716>, and Fisher z 
  transformed partial correlations <doi:10.1111/bmsp.12173>. Parameter uncertainty, 
  predictability, and network replicability <doi:10.31234/osf.io/fb4sa> are also implemented.
	"""
	
	cran = "GGMnonreg" 

	version("1.0.0", md5="0c363000f262db3efb1966cc9a318eef")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-bestglm", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-poibin", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmncv", type=("build", "run"))
