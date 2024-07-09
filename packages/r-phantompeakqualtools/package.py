# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RPhantompeakqualtools(RPackage):
    """This package computes informative enrichment and quality measures for
    ChIP-seq/DNase-seq/FAIRE-seq/MNase-seq data."""

    homepage = "https://github.com/kundajelab/phantompeakqualtools"
    url = "https://github.com/kundajelab/phantompeakqualtools/archive/refs/tags/1.2.2.tar.gz"

    version("1.2.2", sha256="b31263b64aefe97bdc4d7fae138f515a7d7a60cd05031d38dd89a10f9ee10cd1")

    depends_on("awk")
    depends_on("samtools")
    depends_on("r", type=("build", "run"))
    depends_on("r-spp@:1.15", type=("build", "run"))
    # For parallel processing
    depends_on("r-snow", type=("build", "run"))
    depends_on("r-snowfall", type=("build", "run"))
    depends_on("r-bitops", type=("build", "run"))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("run_spp.R", prefix.bin)
