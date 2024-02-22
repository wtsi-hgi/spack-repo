# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScapesclassification(RPackage):
	"""User-Defined Classification of Raster Surfaces

	Series of algorithms to translate  users' mental models of seascapes, 
  landscapes and, more generally, of geographic features into computer representations 
  (classifications). Spaces and geographic objects are classified with user-defined 
  rules taking into account spatial data as well as spatial relationships among 
  different classes and objects.
	"""
	
	homepage = "https://github.com/ghTaranto/scapesClassification"
	cran = "scapesClassification" 

	version("1.0.0", md5="7e708aafabcee3ca7d1500ba3135fa3f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
