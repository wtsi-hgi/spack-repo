# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrainkcca(RPackage):
	"""Region-Level Connectivity Network Construction via Kernel
Canonical Correlation Analysis

	It is designed to calculate connection between (among) brain regions and plot connection lines. Also, the summary function is included to summarize group-level connectivity network. Kang, Jian (2016) <doi:10.1016/j.neuroimage.2016.06.042>.
	"""
	
	cran = "brainKCCA" 

	version("0.1.0", md5="4b54e5f13f9f9c24bc950496bfbde39f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cca", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-brainr", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
