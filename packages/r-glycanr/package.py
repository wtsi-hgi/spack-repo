# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlycanr(RPackage):
	"""Tools for Analysing N-Glycan Data

	Useful utilities in N-glycan data analysis. This package tries
    to fill the gap in N-glycan data analysis by providing easy
    to use functions for basic operations on data
    (see <https://en.wikipedia.org/wiki/Glycomics> for more
    details on Glycomics). At the moment 'glycanr' is mostly oriented
    to data obtained by UPLC (Ultra Performance Liquid Chromatography)
    and LCMS (Liquid chromatography–mass spectrometry)
    analysis of Plasma and IgG glycome.
	"""
	
	homepage = "https://github.com/iugrina/glycanr"
	cran = "glycanr" 

	version("0.4.0", md5="fa02ccf42efa1e31001e606fe2c4cca7")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
