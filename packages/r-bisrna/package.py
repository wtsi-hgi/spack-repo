# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBisrna(RPackage):
	"""Analysis of RNA Cytosine-5 Methylation

	Bisulfite-treated RNA non-conversion in a set of samples is
  analysed as follows : each sample's non-conversion distribution is
  identified to a Poisson distribution. P-values adjusted for multiple
  testing are calculated in each sample. Combined non-conversion P-values
  and standard errors are calculated on the intersection of the set of
  samples. For further details, see C Legrand, F Tuorto, M Hartmann, 
  R Liebers, D Jakob, M Helm and F Lyko (2017) <doi:10.1101/gr.210666.116>.
	"""
	
	cran = "BisRNA" 

	version("0.2.2", md5="3088fcb8f7c282acf7e69031987d787d")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
