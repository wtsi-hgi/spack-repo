# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWyzCodeRdoc(RPackage):
	"""Wizardry Code Offensive Programming R Documentation

	Allows to generate on-demand or by batch, any R documentation file,
    whatever is kind, data, function, class or package. It populates
    documentation sections, either automatically or by considering
    your input. Input code could be standard R code or offensive programming code. 
    Documentation content completeness depends on the type of code you use. With
    offensive programming code, expect generated documentation to be fully 
    completed, from a format and content point of view. With some standard R 
    code, you will have to activate post processing to fill-in any section that 
    requires complements. Produced manual page validity is automatically tested 
    against R documentation compliance rules. Documentation language 
    proficiency, wording style, and phrasal adjustments remains your job. 
	"""
	
	homepage = "https://neonira.github.io/offensiveProgrammingBook_v1.2.2/"
	cran = "wyz.code.rdoc" 

	version("1.1.19", md5="b2f320d06eec3320d84421903011f5ed")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-wyz-code-offensiveprogramming@1.1.22:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-digest@0.6.23:", type=("build", "run"))
