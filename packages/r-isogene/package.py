# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsogene(RPackage):
	"""Order-Restricted Inference for Microarray Experiments

	Offers framework for testing for monotonic relationship between gene expression and doses in a microarray experiment. Several testing procedures including the global likelihood-ratio test (Bartholomew, 1961), Williams (1971, 1972), Marcus (1976), M (Hu et al. 2005) and the modified M (Lin et al. 2007) are used to test for the monotonic trend in gene expression with respect to doses. BH (Benjamini and Hochberg 1995) and BY (Benjamini and Yekutieli 2004) FDR controlling procedures are applied to adjust the raw p-values obtained from the permutations.   
	"""
	
	cran = "IsoGene" 

	version("1.0-24", md5="43434eaeecb7d4cc9f26f30160c3478e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-ff@2:", type=("build", "run"))
