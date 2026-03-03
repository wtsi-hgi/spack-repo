# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRidge(RPackage):
	"""Ridge Regression with Automatic Selection of the Penalty
Parameter

	Linear and logistic ridge regression functions. Additionally includes special functions for 
            genome-wide single-nucleotide polymorphism (SNP) data. More details can be found in
            <doi: 10.1002/gepi.21750> and <doi: 10.1186/1471-2105-12-372>.
	"""
	
	homepage = "https://github.com/SteffenMoritz/ridge"
	cran = "ridge" 

	version("3.3", md5="053bb22425561b8ff6e91bf4e8ad50d5")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("gsl@1.14:", type=("build", "link", "run"))
