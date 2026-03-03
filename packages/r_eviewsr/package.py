# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REviewsr(RPackage):
	"""A Seamless Integration of 'EViews' and R

	It allows running 'EViews' (<https://eviews.com>) program from R, R Markdown and Quarto documents. 'EViews' (Econometric Views) is a statistical software for Econometric analysis.  This package integrates 'EViews' and R and also serves as an 'EViews' Knit-Engine for 'knitr' package. Write all your 'EViews' commands in R, R Markdown or Quarto documents. For details,  please consult our peer-review article Mati S., Civcir I. and Abba S.I (2023) <doi:10.32614/RJ-2023-045>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=EviewsR"
	cran = "EviewsR" 

	version("0.1.6", md5="eff826eb73011d6fb0438ae0109154bf")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
