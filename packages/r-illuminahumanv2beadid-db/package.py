# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanv2beadidDb(RPackage):
    """Illumina HumanWGv2 annotation data (chip illuminaHumanv2BeadID)

    Illumina HumanWGv2 annotation data (chip illuminaHumanv2BeadID) assembled using data from public repositories to be used with data summarized from bead-level data with numeric ArrayAddressIDs as keys. Illumina probes with a No match or Bad quality score were removed prior to annotation. See http://www.compbio.group.cam.ac.uk/Resources/Annotation/index.html and Barbosa-Morais et al (2010) A re-annotation pipeline for Illumina BeadArrays: improving the interpretation of gene expression data. Nucleic Acids Research.
    """

    bioc = "illuminaHumanv2BeadID.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaHumanv2BeadID.db_1.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaHumanv2BeadID.db/illuminaHumanv2BeadID.db_1.8.0.tar.gz",
    ]

    version(
        "1.8.0",
        sha256="97eaec071013942ee2f2d005a50b34dae7afda591fd719df2f76012036b61f11",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@2.4.5:", type=("build", "run"))
