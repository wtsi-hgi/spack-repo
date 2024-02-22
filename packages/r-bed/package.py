# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBed(RPackage):
	"""Biological Entity Dictionary (BED)

	An interface for the 'Neo4j' database providing
    mapping between different identifiers of biological entities.
    This Biological Entity Dictionary (BED)
    has been developed to address three main challenges.
    The first one is related to the completeness of identifier mappings.
    Indeed, direct mapping information provided by the different systems
    are not always complete and can be enriched by mappings provided by other
    resources.
    More interestingly, direct mappings not identified by any of these
    resources can be indirectly inferred by using mappings to a third reference.
    For example, many human Ensembl gene ID are not directly mapped to any
    Entrez gene ID but such mappings can be inferred using respective mappings
    to HGNC ID. The second challenge is related to the mapping of deprecated
    identifiers. Indeed, entity identifiers can change from one resource
    release to another. The identifier history is provided by some resources,
    such as Ensembl or the NCBI, but it is generally not used by mapping tools.
    The third challenge is related to the automation of the mapping process
    according to the relationships between the biological entities of interest.
    Indeed, mapping between gene and protein ID scopes should not be done
    the same way than between two scopes regarding gene ID.
    Also, converting identifiers from different organisms should be possible
    using gene orthologs information.
    The method has been published by
    Godard and van Eyll (2018) <doi:10.12688/f1000research.13925.3>.
	"""
	
	homepage = "https://patzaw.github.io/BED/"
	cran = "BED" 

	version("1.5.0", md5="18bebc011709e1fe5734f8129ff90a4c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-neo2r@2.4.1:", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
