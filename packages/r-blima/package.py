# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlima(RPackage):
	"""Tools for the preprocessing and analysis of the Illumina microarrays on the detector (bead) level

	Package blima includes several algorithms for the preprocessing of Illumina microarray data. It focuses to the bead level analysis and provides novel approach to the quantile normalization of the vectors of unequal lengths. It provides variety of the methods for background correction including background subtraction, RMA like convolution and background outlier removal. It also implements variance stabilizing transformation on the bead level. There are also implemented methods for data summarization. It also provides the methods for performing T-tests on the detector (bead) level and on the probe level for differential expression testing.
	"""
	
	homepage = "https://bitbucket.org/kulvait/blima"
	bioc = "blima"

	version("1.42.0", commit="9ab86a5530c07a3c78e31efdc04b28ef15e03ea6")
	version("1.36.0", commit="21da661384b9762bf4e41e4ea91a6236a84a710a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-beadarray@2:", type=("build", "run"))
	depends_on("r-biobase@2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
