# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomeadmixr(RPackage):
	"""Simulate Admixture of Genomes

	Individual-based simulations forward in time,
    simulating how patterns in ancestry along the genome change after
    admixture. Full description can be found in Janzen (2021)
    <doi:10.1111/2041-210X.13612>.
	"""
	
	homepage = "https://github.com/thijsjanzen/GenomeAdmixR"
	cran = "GenomeAdmixR" 

	version("2.1.7", md5="91d3d272d9f60beca93760f6d7ddf810")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-hierfstat", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
