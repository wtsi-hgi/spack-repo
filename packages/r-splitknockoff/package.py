# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplitknockoff(RPackage):
	"""Split Knockoffs for Structural Sparsity

	Split Knockoff is a data adaptive variable selection framework for controlling the
             (directional) false discovery rate (FDR) in structural sparsity, where variable 
             selection on linear transformation of parameters is of concern. This proposed scheme
             relaxes the linear subspace constraint to its neighborhood, often known as variable
             splitting in optimization.
             Simulation experiments can be reproduced following the Vignette. We include data
             (both .mat and .csv format) and application with our method of Alzheimer's Disease 
             study in this package.
             'Split Knockoffs' is first defined in Cao et al. (2021) <arXiv:2103.16159>. 
	"""
	
	homepage = "https://github.com/wanghaoxue0/SplitKnockoff"
	cran = "SplitKnockoff" 

	version("1.2", md5="6c1c266e951844429a1dc3848da19fb7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
