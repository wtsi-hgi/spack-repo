# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsmap(RPackage):
	"""Linkage Map Construction using the MSTmap Algorithm

	Functions for Accurate and Speedy linkage map construction, manipulation and diagnosis of Doubled Haploid, Backcross and Recombinant Inbred 'R/qtl' objects. This includes extremely fast linkage map clustering and optimal marker ordering using 'MSTmap' (see Wu et al.,2008).
	"""
	
	cran = "ASMap" 

	version("1.0-7", md5="44e5f6168c4ed8db85d54f97c2d421bb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
