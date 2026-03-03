# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrab(RPackage):
	"""How to Add Two Tables

	Methods to "add" two tables; also an alternative
     interpretation of named vectors as generalized tables, so that
     c(a=1,b=2,c=3) + c(b=3,a=-1) will return c(b=5,c=3).  Uses
     'disordR' discipline (Hankin, 2022, <arxiv:2210.03856>).
     Extraction and replacement methods are provided.  The underlying
     mathematical structure is the Free Abelian group, hence the name.
     To cite in publications please use Hankin (2023)
     <arxiv:2307:13184>.
	"""
	
	homepage = "https://github.com/RobinHankin/frab"
	cran = "frab" 

	version("0.0-3", md5="fae7f8f489e453310f40e39b9cdf231d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-disordr@0.9.8.1:", type=("build", "run"))
