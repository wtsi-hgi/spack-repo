# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossva(RPackage):
	"""Verbal Autopsy Data Transformation for InSilicoVA and InterVA5
Algorithms

	Enables transformation of Verbal Autopsy data collected with the WHO 2016 questionnaire (versions 1.4.1 & 1.5.1)
  or the WHO 2014 questionnaire for automated coding of Cause of Death using the InSilicoVA (data.type = "WHO2016") and
  InterVA5 algorithms. Previous versions of this package supported user-supplied mappings (via the map_records function), but
  this functionality has been removed.  This package is made available by WHO and the Bloomberg Data for Health Initiative.
	"""
	
	cran = "CrossVA" 

	version("1.0.0", md5="b3e4072b800d26b94ebd22efce238c4b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
