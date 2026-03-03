# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatcont(RPackage):
	"""Test, Identify, Select and Mutate Categorical or Continuous
Values

	Methods and utilities for testing, identifying, selecting and  
    mutating objects as categorical or continous types. These functions work on both 
    atomic vectors as well as recursive objects: data.frames, data.tables, 
    tibbles, lists, etc.. 
	"""
	
	homepage = "https://github.com/decisionpatterns/catcont"
	cran = "catcont" 

	version("0.5.0", md5="84424ccda8821587d976e712f42e2f45")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
