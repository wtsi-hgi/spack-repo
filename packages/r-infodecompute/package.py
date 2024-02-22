# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfodecompute(RPackage):
	"""Information Decomposition of Two-Phase Experiments

	The main purpose of this package is to generate the structure of the analysis of variance 
            (ANOVA) table of the two-phase experiments. The user only need to input the design and the 
              relationships of the random and fixed factors using the Wilkinson-Rogers' syntax, 
              this package can then quickly generate the structure of the ANOVA table with the 
              coefficients of the variance components for the expected mean squares.
              Thus, the balanced incomplete block design and provides the efficiency
              factors of the fixed effects can also be studied and compared much easily.
	"""
	
	homepage = "https://github.com/kcha193/infoDecompuTE"
	cran = "infoDecompuTE" 

	version("0.6.2", md5="28ccfdd5c64458b04678f8ce6c610a97")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
