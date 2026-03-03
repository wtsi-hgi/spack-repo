# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputemulti(RPackage):
	"""Imputation Methods for Multivariate Multinomial Data

	Implements imputation methods using EM and Data Augmentation for
    multinomial data following the work of Schafer 1997 <ISBN: 978-0-412-04061-0>.
	"""
	
	cran = "imputeMulti" 

	version("0.8.4", md5="a6938607a821df789f87f461a5ead531")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
