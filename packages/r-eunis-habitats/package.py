# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REunisHabitats(RPackage):
	"""EUNIS Habitat Classification

	The EUNIS habitat classification is a comprehensive pan-European
    system for habitat identification
    <https://www.eea.europa.eu/data-and-maps/data/eunis-habitat-classification-1>.
    This is an R data package providing the EUNIS classification system.
    The classification is hierarchical and covers all types of habitats from
    natural to artificial, from terrestrial to freshwater and marine. The
    habitat types are identified by specific codes, names and descriptions and
    come with schema crosswalks to other habitat typologies.
	"""
	
	homepage = "https://github.com/ramiromagno/eunis.habitats"
	cran = "eunis.habitats" 

	version("0.1.0", md5="59252d96ffc8ec4a3d0919c9ebce6e2e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
