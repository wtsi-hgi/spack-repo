# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinytest2junit(RPackage):
	"""Convert 'tinytest' Output to JUnit XML

	Unit testing is a solid component of automated CI/CD pipelines. 'tinytest' - a light-weight,
	zero-dependency  alternative to 'testthat' was developed. To be able to integrate 'tinytests' results into common CI/CD
	systems the 'tinytests'-object needs to be converted to JUnit XML format. 'tinytest2JUnit' enables this conversion
	while keeping the zero-dependency nature.
	"""
	
	homepage = "https://github.com/openanalytics/tinytest2JUnit"
	cran = "tinytest2JUnit" 

	version("1.0.1", md5="bb9d0cd46fe6f35143266f4cd5ad18fd")

