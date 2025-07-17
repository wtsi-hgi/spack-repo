# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcluderanges(RPackage):
    """Genomic coordinates of problematic genomic regions

    Genomic coordinates of problematic genomic regions that should be avoided when working with genomic data. GRanges of exclusion regions (formerly known as blacklisted), centromeres, telomeres, known heterochromatin regions, etc. (UCSC 'gap' table data). Primarily for human and mouse genomes, hg19/hg38 and mm9/mm10 genome assemblies.
    """

    homepage = "https://github.com/dozmorovlab/excluderanges"
    bioc = "excluderanges"

    version("0.99.8", commit="f53e82dfbbc1e614fcb4bd23849493566e0165cb")
    version("0.99.8", commit="f53e82dfbbc1e614fcb4bd23849493566e0165cb")

    depends_on("r-genomicranges", type=("build", "run"))
