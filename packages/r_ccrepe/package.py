# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcrepe(RPackage):
	"""ccrepe_and_nc.score

	The CCREPE (Compositionality Corrected by REnormalizaion and PErmutation) package is designed to assess the significance of general similarity measures in compositional datasets.  In microbial abundance data, for example, the total abundances of all microbes sum to one; CCREPE is designed to take this constraint into account when assigning p-values to similarity measures between the microbes.  The package has two functions: ccrepe: Calculates similarity measures, p-values and q-values for relative abundances of bugs in one or two body sites using bootstrap and permutation matrices of the data. nc.score: Calculates species-level co-variation and co-exclusion patterns based on an extension of the checkerboard score to ordinal data.
	"""
	
	bioc = "ccrepe" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ccrepe_1.38.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ccrepe/ccrepe_1.38.1.tar.gz"]

	version("1.38.1", md5="151d956c2fbdaaf64fccbea7f4905a2d")

	depends_on("r-infotheo@1.1:", type=("build", "run"))
