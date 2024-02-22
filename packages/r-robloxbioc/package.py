# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobloxbioc(RPackage):
	"""Infinitesimally Robust Estimators for Preprocessing -Omics Data

	Functions for the determination of optimally robust influence curves and
             estimators for preprocessing omics data, in particular gene expression data
             (Kohl and Deigner (2010), <doi:10.1186/1471-2105-11-583>).
	"""
	
	homepage = "https://r-forge.r-project.org/projects/robast/"
	cran = "RobLoxBioC" 

	version("1.2.2", md5="9432a6f111603336b31554e600c71fea")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distr@2.8:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-beadarray", type=("build", "run"))
	depends_on("r-roblox@1.1:", type=("build", "run"))
	depends_on("r-distrmod@2.8:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
