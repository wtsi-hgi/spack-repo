# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWyzCodeTestthat(RPackage):
	"""Wizardry Code Offensive Programming Test Generation

	Allows to generate automatically 'testthat' code files from offensive 
    programming test cases. Generated test files are complete and ready to run.
    Using 'wyz.code.testthat' you will earn a lot of time, reduce the number of
    errors in test case production, be able to test immediately generated files 
    without any need to view or modify them, and enter a zero time latency between 
    code implementation and industrial testing. As with 'testthat', you may
    complete provided test cases according to your needs to push testing further, 
    but this need is nearly void when using 'wyz.code.offensiveProgramming'. 
	"""
	
	homepage = "https://neonira.github.io/offensiveProgrammingBook_v1.2.2/"
	cran = "wyz.code.testthat" 

	version("1.1.20", md5="d338a9e48c95b7260afaf0080262c590")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-wyz-code-offensiveprogramming@1.1.22:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
