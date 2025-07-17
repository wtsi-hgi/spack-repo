# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtbls2(RPackage):
    """MetaboLights MTBLS2: Comparative LC/MS-based profiling of silver nitrate-treated Arabidopsis thaliana leaves of wild-type and cyp79B2 cyp79B3 double knockout plants. Böttcher et al. (2004)

    Indole-3-acetaldoxime (IAOx) represents an early intermediate of the biosynthesis of a variety of indolic secondary metabolites including the phytoanticipin indol-3-ylmethyl glucosinolate and the phytoalexin camalexin (3-thiazol-2'-yl-indole). Arabidopsis thaliana cyp79B2 cyp79B3 double knockout plants are completely impaired in the conversion of tryptophan to indole-3-acetaldoxime and do not accumulate IAOx-derived metabolites any longer. Consequently, comparative analysis of wild-type and cyp79B2 cyp79B3 plant lines has the potential to explore the complete range of IAOx-derived indolic secondary metabolites.
    """

    homepage = "http://www.ebi.ac.uk/metabolights/MTBLS2"
    bioc = "mtbls2"

    version("1.38.0", commit="c24e66e43543badc43272110c99b93bf80bd6d2e")
    version("1.32.0", commit="cf4084283d8ed8657335f2e430dc54a3bdcddfb3")

    depends_on("r@2.10:", type=("build", "run"))
