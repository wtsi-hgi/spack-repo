# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAshkenazimsonchr21(RPackage):
    """Annotated variants on the chromosome 21, human genome 19, Ashkenazim Trio son sample

    SonVariantsChr21 is a dataset of annotated genomic variants coming from Complete Genomics whole genome sequencing. Data comes from GIAB project, Ashkenazim Trio, sample HG002 run 1. Both vcf and annotated data frame are provided.
    """

    bioc = "AshkenazimSonChr21"

    version("1.38.0", commit="8d96b53ac12de6e98aa48f51cfa9777836426c8a")
    version("1.32.0", commit="798ba4155c9398f4faed449579fe2f43cb47414f")
