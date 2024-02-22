# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyspcTestthat(RPackage):
	"""'testthat' Unit Test Enhancements

	Enhance package 'testthat' by allowing tests to be attached to the function/object they test. 
    This allows to keep functional and unit test code together.
	"""
	
	cran = "hySpc.testthat" 

	version("0.2.1", md5="708528bea445caa4099a21bd65d87f33")

	depends_on("r-testthat", type=("build", "run"))
