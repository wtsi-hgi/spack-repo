# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorx(RPackage):
	"""Create and Format Correlation Matrices

	Create correlation (or partial correlation) matrices. Correlation matrices are formatted with significance stars based on user preferences. Matrices of coefficients, p-values, and number of pairwise observations are returned. Send resultant formatted matrices to the clipboard to be pasted into excel and other programs. A plot method allows users to visualize correlation matrices created with 'corx'.
	"""
	
	homepage = "https://github.com/conig/corx"
	cran = "corx" 

	version("1.0.7.2", md5="6b6a5f8767b6444dd7206bdb78d2dbcc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
