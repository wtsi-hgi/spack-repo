# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcsstools(RPackage):
	"""Tools for Regression Using Pre-Computed Summary Statistics

	Defines functions to describe regression models using only
    pre-computed summary statistics (i.e. means, variances, and covariances)
    in place of individual participant data.
    Possible models include linear models for linear combinations, products, 
    and logical combinations of phenotypes.
    Implements methods presented in 
    Wolf et al. (2021) <doi:10.3389/fgene.2021.745901>
    Wolf et al. (2020) <doi:10.1142/9789811215636_0063> and 
    Gasdaska et al. (2019) <doi:10.1142/9789813279827_0036>.
	"""
	
	homepage = "https://github.com/jackmwolf/pcsstools/"
	cran = "pcsstools" 

	version("0.1.2", md5="00bbc4b9b0f16773c1996ef31ee4e068")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
