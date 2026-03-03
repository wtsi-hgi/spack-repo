# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSumfregat(RPackage):
	"""Fast Region-Based Association Tests on Summary Statistics

	An adaptation of classical region/gene-based association analysis
    techniques to the use of summary statistics (P values and effect sizes)
    and correlations between genetic variants as input. It is a tool to perform
    the most popular and efficient gene-based tests using the results of genome-wide
    association (meta-)analyses without having the original genotypes and
    phenotypes at hand.
    See for details:
    Svishcheva et al (2019) Gene-based association tests using GWAS summary
    statistics. Bioinformatics.
    Belonogova et al (2022) SumSTAAR: A flexible framework for gene-based
    association studies using GWAS summary statistics. PLOS Comp Biol.
	"""
	
	cran = "sumFREGAT" 

	version("1.2.5", md5="91609e83136b9858759291bb391080b5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-seqminer", type=("build", "run"))
	depends_on("r-gbj", type=("build", "run"))
