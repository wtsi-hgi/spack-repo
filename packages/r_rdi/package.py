# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdi(RPackage):
	"""Repertoire Dissimilarity Index

	Methods for calculation and visualization of the Repertoire
    Dissimilarity Index. Citation: Bolen and Rubelt, et al (2017) 
    <doi:10.1186/s12859-017-1556-5>.
	"""
	
	homepage = "http://rdi.readthedocs.io"
	cran = "rdi" 

	version("1.0.0", md5="27228a1b41bb9101eb86e043a6d8ffcc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-beanplot", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
