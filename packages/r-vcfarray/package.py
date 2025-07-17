# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcfarray(RPackage):
    """Representing on-disk / remote VCF files as array-like objects

    VCFArray extends the DelayedArray to represent VCF data entries as array-like objects with on-disk / remote VCF file as backend. Data entries from VCF files, including info fields, FORMAT fields, and the fixed columns (REF, ALT, QUAL, FILTER) could be converted into VCFArray instances with different dimensions.
    """

    homepage = "https://github.com/Liubuntu/VCFArray"
    bioc = "VCFArray"

    version("1.24.0", commit="b36ef193d108f41c3c5dc031d6e36913b11240b3")
    version("1.18.0", commit="83c4b58b7b18d128953ff0eeb43b41d5aef54fa2")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-delayedarray@0.7.28:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-variantannotation@1.29.3:", type=("build", "run"))
    depends_on("r-genomicfiles@1.17.3:", type=("build", "run"))
    depends_on("r-s4vectors@0.19.19:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
