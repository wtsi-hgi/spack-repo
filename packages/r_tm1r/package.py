# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTm1r(RPackage):
	"""The Integration Between 'IBM COGNOS TM1' and R

	Useful functions to connect to 'TM1' <https://www.ibm.com/uk-en/products/planning-and-analytics> instance from R via REST API. With the functions in the package, data can be imported from 'TM1' via mdx view or native view, data can be sent to 'TM1', processes and chores can be executed, and cube and dimension metadata information can be taken. 
	"""
	
	homepage = "https://github.com/muhammedalionder/tm1r"
	cran = "tm1r" 

	version("1.1.8", md5="fb7b94d27c70750140be43830e1e82f8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
