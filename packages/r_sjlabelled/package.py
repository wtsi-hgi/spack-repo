# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSjlabelled(RPackage):
	"""Labelled Data Utility Functions

	Collection of functions dealing with labelled data, like reading and 
    writing data between R and other statistical software packages like 'SPSS',
    'SAS' or 'Stata', and working with labelled data. This includes easy ways 
    to get, set or change value and variable label attributes, to convert 
    labelled vectors into factors or numeric (and vice versa), or to deal with 
    multiple declared missing values.
	"""
	
	homepage = "https://strengejacke.github.io/sjlabelled/"
	cran = "sjlabelled" 

	version("1.2.0", md5="116f5e31e52014c92ed17f3ffaeb7a09")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-datawizard", type=("build", "run"))
