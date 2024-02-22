# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistfreeCr(RPackage):
	"""Distribution-Free Confidence Region

	Constructs confidence regions without the need to know the sampling distribution of bivariate data. The method was proposed by Zhiqiu Hu & Rong-cai Yang (2013) <doi:10.1371/journal.pone.0081179.g001>. 
	"""
	
	homepage = "http://statgen.ualberta.ca"
	cran = "distfree.cr" 

	version("1.5.1", md5="5ae2de78cd1dec715cb18e99faff0e83")

	depends_on("r@2.10:", type=("build", "run"))
