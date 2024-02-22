# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RA3(RPackage):
	"""Accurate, Adaptable, and Accessible Error Metrics for Predictive
Models

	Supplies tools for tabulating and analyzing the results of predictive models. The methods employed are applicable to virtually any predictive model and make comparisons between different methodologies straightforward.
	"""
	
	cran = "A3" 

	version("1.0.0", md5="027ebdd8affce8f0effaecfcd5f5ade2", url="https://cran.r-project.org/src/contrib/A3_1.0.0.tar.gz")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
