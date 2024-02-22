# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompoundevents(RPackage):
	"""Statistical Modeling of Compound Events

	Tools for extracting occurrences, assessing potential driving factors, predicting occurrences, and quantifying impacts of compound events in hydrology and climatology. Please see Hao Zengchao et al. (2019) <doi:10.1088/1748-9326/ab4df5>. 
	"""
	
	cran = "CompoundEvents" 

	version("0.3.0", md5="160325f820f0441bece7e36206cf75af")

	depends_on("r@3.5:", type=("build", "run"))
