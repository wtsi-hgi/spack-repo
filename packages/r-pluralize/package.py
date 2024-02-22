# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPluralize(RPackage):
	"""Pluralize and 'Singularize' Any (English) Word

	Tools are provided to create plural, singular and regular forms of 
    English words along with tools to augment the built-in rules to fit 
    specialized needs. Core functionality is based on a JavaScript library, 
    <https://github.com/blakeembrey/pluralize>.
	"""
	
	homepage = "http://gitlab.com/hrbrmstr/pluralize"
	cran = "pluralize" 

	version("0.2.0", md5="084afd57afa2a13c330cea17a9ca90b2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
