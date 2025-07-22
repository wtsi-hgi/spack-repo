# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurfaltr(RPackage):
    """Rapid Comparison of Surface Protein Isoform Membrane Topologies Through surfaltr

    Cell surface proteins form a major fraction of the druggable proteome and can be used for tissue-specific delivery of oligonucleotide/cell-based therapeutics. Alternatively spliced surface protein isoforms have been shown to differ in their subcellular localization and/or their transmembrane (TM) topology. Surface proteins are hydrophobic and remain difficult to study thereby necessitating the use of TM topology prediction methods such as TMHMM and Phobius. However, there exists a need for bioinformatic approaches to streamline batch processing of isoforms for comparing and visualizing topologies. To address this gap, we have developed an R package, surfaltr. It pairs inputted isoforms, either known alternatively spliced or novel, with their APPRIS annotated principal counterparts, predicts their TM topologies using TMHMM or Phobius, and generates a customizable graphical output. Further, surfaltr facilitates the prioritization of biologically diverse isoform pairs through the incorporation of three different ranking metrics and through protein alignment functions. Citations for programs mentioned here can be found in the vignette.
    """

    bioc = "surfaltr"

    version("1.14.0", commit="153eb5f7c25dde1fcd9de0f1bbfba4ba62317601")
    version("1.8.0", commit="9dfbbafc32323fb790bb2d87b12e355bca2053ad")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-dplyr@1.0.6:", type=("build", "run"))
    depends_on("r-biomart@2.46:", type=("build", "run"))
    depends_on("r-protr@1.6.2:", type=("build", "run"))
    depends_on("r-seqinr@4.2.5:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
    depends_on("r-stringr@1.4:", type=("build", "run"))
    depends_on("r-biostrings@2.58:", type=("build", "run"))
    depends_on("r-readr@1.4:", type=("build", "run"))
    depends_on("r-httr@1.4.2:", type=("build", "run"))
    depends_on("r-testthat@3:", type=("build", "run"))
    depends_on("r-xml2@1.3.2:", type=("build", "run"))
    depends_on("r-msa@1.22:", type=("build", "run"))
