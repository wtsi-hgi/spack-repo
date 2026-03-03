# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorr2d(RPackage):
	"""Implementation of 2D Correlation Analysis in R

	Implementation of two-dimensional (2D) correlation analysis based
    on the Fourier-transformation approach described by Isao Noda (I. Noda
    (1993) <DOI:10.1366/0003702934067694>). Additionally there are two plot
    functions for the resulting correlation matrix: The first one creates
    colored 2D plots, while the second one generates 3D plots.
	"""
	
	cran = "corr2D" 

	version("1.0.3", md5="e55ac579d17558ef8285ba0ef374a164")

	depends_on("r-doparallel@1.0.8:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-fields@8.2.1:", type=("build", "run"))
	depends_on("r-mmand@1.3:", type=("build", "run"))
	depends_on("r-colorspace@1.3.0:", type=("build", "run"))
