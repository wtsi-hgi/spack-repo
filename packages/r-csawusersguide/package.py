# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsawusersguide(RPackage):
    """csaw User's Guide

    A user's guide for the csaw package for detecting differentially bound regions in ChIP-seq data. Describes how to read in BAM files to obtain a per-window count matrix, filtering to obtain high-abundance windows of interest, normalization of sample-specific biases, testing for differential binding, consolidation of per-window results to obtain per-region statistics, and annotation and visualization of the DB results.
    """

    bioc = "csawUsersGuide"

    version("1.24.0", commit="5f5cdc62add3335e8a2e2fbdc981fa3facf50d72")
    version("1.18.0", commit="9c34d2e91e3d3e1f30990c265c413a89ae9774b0")
