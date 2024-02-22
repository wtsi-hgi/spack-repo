# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCotram(RPackage):
	"""Count Transformation Models

	Count transformation models featuring 
        parameters interpretable as discrete hazard ratios, odds ratios,
        reverse-time discrete hazard ratios, or transformed expectations. 
        An appropriate data transformation for a count outcome and
        regression coefficients are simultaneously estimated by maximising
        the exact discrete log-likelihood using the computational framework
        provided in package 'mlt', technical details are given in
        Siegfried & Hothorn (2020) <DOI:10.1111/2041-210X.13383>. 
        The package also contains an experimental implementation of 
        multivariate count transformation models with an application
        to multi-species distribution models <arXiv:2201.13095>.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "cotram" 

	version("0.4-4", md5="d5d262217c376dc6ecd42fb6670cb2cd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tram@0.8.0:", type=("build", "run"))
	depends_on("r-mlt@1.2.1:", type=("build", "run"))
	depends_on("r-variables@1.0.2:", type=("build", "run"))
	depends_on("r-basefun@1.0.5:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
