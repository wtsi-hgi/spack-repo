# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcr(RPackage):
	"""Functional Concurrent Regression for Sparse Data

	Dynamic prediction in functional concurrent regression with an application to child growth. Extends the pffr() function from the 'refund' package to handle the scenario where the functional response and concurrently measured functional predictor are irregularly measured.  Leroux et al. (2017), Statistics in Medicine, <doi:10.1002/sim.7582>.
	"""
	
	cran = "fcr" 

	version("1.0", md5="23deeaca25804e56d3f06e11b2fbaa24")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-face@0.1:", type=("build", "run"))
	depends_on("r-mgcv@1.7:", type=("build", "run"))
	depends_on("r-fields@9:", type=("build", "run"))
