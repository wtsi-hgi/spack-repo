# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDominoeffect(RPackage):
    """Identification and Annotation of Protein Hotspot Residues

    The functions support identification and annotation of hotspot residues in proteins. These are individual amino acids that accumulate mutations at a much higher rate than their surrounding regions.
    """

    bioc = "DominoEffect"

    version("1.28.0", commit="197b3ec6e1040f48da7c0fbfeb1f3c2bdc117fcd")
    version("1.22.0", commit="58dcf550710cd65efe14d17e76890e60843aa219")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
