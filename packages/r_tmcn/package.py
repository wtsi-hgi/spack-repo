# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmcn(RPackage):
	"""A Text Mining Toolkit for Chinese

	A Text mining toolkit for Chinese, which includes facilities for 
    Chinese string processing, Chinese NLP supporting, encoding detecting and 
    converting. Moreover, it provides some functions to support 'tm' package 
    in Chinese.
	"""
	
	cran = "tmcn" 

	version("0.2-13", md5="5426a3cf63d80d27835b48e95dadb4a3")

	depends_on("r@3:", type=("build", "run"))
