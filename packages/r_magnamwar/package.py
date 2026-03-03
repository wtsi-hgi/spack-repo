# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagnamwar(RPackage):
	"""A Pipeline for Meta-Genome Wide Association

	Correlates variation within the meta-genome to target species
    phenotype variations in meta-genome with association studies. Follows
    the pipeline described in Chaston, J.M. et al. (2014) <doi:10.1128/mBio.01631-14>.
	"""
	
	cran = "MAGNAMWAR" 

	version("2.0.4", md5="02e12ff9e1592b08203cdd56fbb8fa77")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-coxme", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
