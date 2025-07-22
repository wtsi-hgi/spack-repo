# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetscanMmEgDb(RPackage):
    """TargetScan miRNA target predictions for mouse

    TargetScan miRNA target predictions for mouse assembled using data from the TargetScan website. TargetScan predicts biological targets of miRNAs by searching for the presence of conserved 8mer and 7mer sites that match the seed region of each miRNA. Also identified are sites with mismatches in the seed region that are compensated by conserved 3' pairing. In mammals, predictions are ranked based on the predicted efficacy of targeting as calculated using the context scores of the sites.
    """

    bioc = "targetscan.Mm.eg.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/targetscan.Mm.eg.db_0.6.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/targetscan.Mm.eg.db/targetscan.Mm.eg.db_0.6.1.tar.gz",
    ]

    version(
        "0.6.1",
        sha256="c5b1f49bdf7755fecc0cc0f6a536997160f0380d9ef19b1916a827cb6fdfa629",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
