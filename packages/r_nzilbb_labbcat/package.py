# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNzilbbLabbcat(RPackage):
	"""Accessing Data Stored in 'LaBB-CAT' Instances

	'LaBB-CAT' is a web-based language corpus management
 system developed by the New Zealand Institute of Language, Brain
 and Behaviour (NZILBB) - see <https://labbcat.canterbury.ac.nz>.
 This package defines functions for accessing corpus data in a 'LaBB-CAT'
 instance. You must have at least version 20230224.1731 of 'LaBB-CAT'
 to use this package.
 For more information about 'LaBB-CAT', see
 Robert Fromont and Jennifer Hay (2008) <doi:10.3366/E1749503208000142>
 or 
 Robert Fromont (2017) <doi:10.1016/j.csl.2017.01.004>.
	"""
	
	homepage = "https://nzilbb.github.io/labbcat-R/"
	cran = "nzilbb.labbcat" 

	version("1.3-0", md5="853db98f8c599bee0ff8965d59388a44")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
