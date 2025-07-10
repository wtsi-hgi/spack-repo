# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParody(RPackage):
	"""Parametric And Resistant Outlier DYtection

	Provide routines for univariate and multivariate outlier detection with a focus on parametric methods, but support for some methods based on resistant statistics.
	"""
	
	bioc = "parody" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/parody_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/parody/parody_1.60.0.tar.gz"]

	version("1.60.0", sha256="5292c5217200bf13e60f8712f14c049fc494f38dfbba337ae54b24e8e15cb016")

	depends_on("r@3.5:", type=("build", "run"))
