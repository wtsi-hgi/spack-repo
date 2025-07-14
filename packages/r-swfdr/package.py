# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwfdr(RPackage):
	"""Estimation of the science-wise false discovery rate and the false discovery rate conditional on covariates

	This package allows users to estimate the science-wise false discovery rate from Jager and Leek, "Empirical estimates suggest most published medical research is true," 2013, Biostatistics, using an EM approach due to the presence of rounding and censoring. It also allows users to estimate the false discovery rate conditional on covariates, using a regression framework, as per Boca and Leek, "A direct approach to estimating false discovery rates conditional on covariates," 2018, PeerJ.
	"""
	
	homepage = "https://github.com/leekgroup/swfdr"
	bioc = "swfdr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/swfdr_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/swfdr/swfdr_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="e3b56e72ab8e081aa5a7c3426e7c6febc5b2d49d47adb6fd48ebcb6836a0ce76")

	depends_on("r@3.4:", type=("build", "run"))
