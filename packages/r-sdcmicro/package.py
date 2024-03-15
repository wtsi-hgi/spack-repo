# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdcmicro(RPackage):
	"""Statistical Disclosure Control Methods for Anonymization of Data
and Risk Estimation

	Data from statistical agencies and other institutions are mostly
    confidential. This package, introduced in Templ, Kowarik and Meindl (2017) <doi:10.18637/jss.v067.i04>, can be used for the generation of anonymized
    (micro)data, i.e. for the creation of public- and scientific-use files.
    The theoretical basis for the methods implemented can be found in Templ (2017) <doi:10.1007/978-3-319-50272-4>.
    Various risk estimation and anonymization methods are included. Note that the package
    includes a graphical user interface published in Meindl and Templ (2019) <doi:10.3390/a12090191> that allows to use various methods of this
    package.
	"""
	
	homepage = "https://github.com/sdcTools/sdcMicro"
	cran = "sdcMicro" 

	version("5.7.8", md5="610d6e7c4210211459ad33f0ebc30185")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-cardata", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-prettydoc", type=("build", "run"))
	depends_on("r-vim@4.7:", type=("build", "run"))
