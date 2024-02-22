# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlcharts(RPackage):
	"""Interactive Graphics for QTL Experiments

	Web-based interactive charts (using D3.js) for the analysis of
    experimental crosses to identify genetic loci (quantitative trait
    loci, QTL) contributing to variation in quantitative traits.
    Broman (2015) <doi:10.1534/genetics.114.172742>.
	"""
	
	homepage = "https://kbroman.org/qtlcharts/"
	cran = "qtlcharts" 

	version("0.16", md5="52fb760ad912c62f217a248719390f65")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-qtl@1.30.4:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
