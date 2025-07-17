# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynapsis(RPackage):
    """An R package to automate the analysis of double-strand break repair during meiosis

    Synapsis is a Bioconductor software package for automated (unbiased and reproducible) analysis of meiotic immunofluorescence datasets. The primary functions of the software can i) identify cells in meiotic prophase that are labelled by a synaptonemal complex axis or central element protein, ii) isolate individual synaptonemal complexes and measure their physical length, iii) quantify foci and co-localise them with synaptonemal complexes, iv) measure interference between synaptonemal complex-associated foci. The software has applications that extend to multiple species and to the analysis of other proteins that label meiotic prophase chromosomes. The software converts meiotic immunofluorescence images into R data frames that are compatible with machine learning methods. Given a set of microscopy images of meiotic spread slides, synapsis crops images around individual single cells, counts colocalising foci on strands on a per cell basis, and measures the distance between foci on any given strand.
    """

    bioc = "synapsis"

    version("1.14.0", commit="e22aa1f03423e51d4124311e9651720adab7a0be")
    version("1.8.0", commit="5a0e387ab7a6ffb95c6bd9bd3f8994283fb5ab21")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-ebimage", type=("build", "run"))
