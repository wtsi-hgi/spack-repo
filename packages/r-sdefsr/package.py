# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdefsr(RPackage):
	"""Subgroup Discovery with Evolutionary Fuzzy Systems

	Implementation of evolutionary fuzzy systems for the data mining task called
    "subgroup discovery". In particular, the algorithms presented in this package are:
    M. J. del Jesus, P. Gonzalez, F. Herrera, M. Mesonero (2007) <doi:10.1109/TFUZZ.2006.890662>
    M. J. del Jesus, P. Gonzalez, F. Herrera (2007) <doi:10.1109/MCDM.2007.369416>
    C. J. Carmona, P. Gonzalez, M. J. del Jesus, F. Herrera (2010) <doi:10.1109/TFUZZ.2010.2060200>
    C. J. Carmona, V. Ruiz-Rodado, M. J. del Jesus, A. Weber, M. Grootveld, P. González, D. Elizondo (2015) <doi:10.1016/j.ins.2014.11.030>
    It also provide a Shiny App to ease the analysis. The algorithms work with data sets provided in
    KEEL, ARFF and CSV format and also with data.frame objects. 
	"""
	
	homepage = "https://github.com/SIMIDAT/SDEFSR"
	cran = "SDEFSR" 

	version("0.7.22", md5="f6a3c9c1b23d3ab7b876d5c4a3494c2e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny@0.11:", type=("build", "run"))
