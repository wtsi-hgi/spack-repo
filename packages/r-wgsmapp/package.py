# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWgsmapp(RPackage):
    """Mappability tracks of Whole-genome Sequencing from the ENCODE Project

    This package provides whole-genome mappability tracks on human hg19/hg38 assembly. We employed the 100-mers mappability track from the ENCODE Project and computed weighted average of the mappability scores if multiple ENCODE regions overlap with the same bin. “Blacklist” bins, including segmental duplication regions and gaps in reference assembly from telomere, centromere, and/or heterochromatin regions are included. The dataset consists of three assembled .bam files of single-cell whole genome sequencing from 10X for illustration purposes.
    """

    bioc = "WGSmapp"

    version("1.20.0", commit="562f0a1f3f061caf45b5f7b8c7722e25864ce858")
    version("1.14.0", commit="ed78a344ccc5d18f7ae87751ef244dda2c09e517")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
