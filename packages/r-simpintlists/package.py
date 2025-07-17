# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimpintlists(RPackage):
    """The package contains BioGRID interactions for various organisms in a simple format

    The package contains BioGRID interactions for arabidopsis(thale cress), c.elegans, fruit fly, human, mouse, yeast( budding yeast ) and S.pombe (fission yeast) . Entrez ids, official names and unique ids can be used to find proteins. The format of interactions are lists. For each gene/protein, there is an entry in the list with "name" containing name of the gene/protein and "interactors" containing the list of genes/proteins interacting with it.
    """

    bioc = "simpIntLists"

    version("1.44.0", commit="85940a5143e979b2673b639a4665e18cd1a7ea65")
    version("1.38.0", commit="c8ebf0513ff06252bcf818b50216afc2259a20e7")
