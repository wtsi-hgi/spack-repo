# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdalpha(RPackage):
	"""Depth-Based Classification and Calculation of Data Depth

	Contains procedures for depth-based supervised learning, which are entirely non-parametric, in particular the DDalpha-procedure (Lange, Mosler and Mozharovskyi, 2014 <doi:10.1007/s00362-012-0488-4>). The training data sample is transformed by a statistical depth function to a compact low-dimensional space, where the final classification is done. It also offers an extension to functional data and routines for calculating certain notions of statistical depth functions. 50 multivariate and 5 functional classification problems are included. (Pokotylo, Mozharovskyi and Dyckerhoff, 2019 <doi:10.18637/jss.v091.i05>).
	"""
	
	cran = "ddalpha" 

	version("1.3.15", md5="eee5e25fb1559d4aebf0c4343c1214c7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
