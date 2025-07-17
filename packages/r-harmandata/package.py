# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmandata(RPackage):
    """Data for the Harman package

    Datasets of accompany Harman, a PCA and constrained optimisation based technique. Contains three example datasets: IMR90, Human lung fibroblast cells exposed to nitric oxide; NPM, an experiment to test skin penetration of metal oxide nanoparticles following topical application of sunscreens in non-pregnant mice; OLF; an experiment to gauge the response of human olfactory neurosphere-derived (hONS) cells to ZnO nanoparticles. Since version 1.24, this package also contains the Infinium5 dataset, a set of batch correction adjustments across 5 Illumina Infinium Methylation BeadChip datasets. This file does not contain methylation data, but summary statistics of 5 datasets after correction. There is also an EpiSCOPE_sample file as exampling for the new methylation clustering functionality in Harman.
    """

    homepage = "http://www.bioinformatics.csiro.au/harman/"
    bioc = "HarmanData"

    version("1.36.0", commit="8f2f2e97fd4ab35a74a4af2f04f10e9741f5a2f7")
    version("1.30.0", commit="b6564736b1918e91a9e1247e4a702b2df8f8e660")

    depends_on("r@3.5:", type=("build", "run"))
