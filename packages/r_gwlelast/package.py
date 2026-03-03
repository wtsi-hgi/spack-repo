# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwlelast(RPackage):
	"""Geographically Weighted Logistic Elastic Net Regression

	Fit a geographically weighted logistic elastic net regression. Detailed explanations can be found in Yoneoka et al. (2016): New algorithm for constructing area-based index with geographical heterogeneities and variable selection: An application to gastric cancer screening <doi:10.1038/srep26582>.
	"""
	
	cran = "GWLelast" 

	version("1.2.2", md5="3cde3a301ff05ac66808fe1ca659dde9")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spgwr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
