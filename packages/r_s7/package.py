# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS7(RPackage):
	"""An Object Oriented System Meant to Become a Successor to S3 and
S4

	A new object oriented programming system designed to be a successor 
  to S3 and S4. It includes formal class, generic, and method specification, 
  and a limited form of multiple dispatch. It has been designed and implemented 
  collaboratively by the R Consortium Object-Oriented Programming Working Group, 
  which includes representatives from R-Core, 'Bioconductor', 
  'Posit'/'tidyverse', and the wider R community.
	"""
	
	homepage = "https://github.com/rconsortium/S7/"
	cran = "S7" 

	version("0.1.1", md5="8f90bb3c2b4e8cf6cb8af4e5a01cc4c4", url="https://cran.r-project.org/src/contrib/S7_0.1.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
