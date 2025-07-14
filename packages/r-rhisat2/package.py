# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhisat2(RPackage):
    """R Wrapper for HISAT2 Aligner

    An R interface to the HISAT2 spliced short-read aligner by Kim et al. (2015). The package contains wrapper functions to create a genome index and to perform the read alignment to the generated index.
    """

    homepage = "https://github.com/fmicompbio/Rhisat2"
    bioc = "Rhisat2"
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rhisat2_1.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rhisat2/Rhisat2_1.18.0.tar.gz",
    ]

    version("1.24.0", tag="RELEASE_3_21")
    version(
        "1.18.0",
        md5="bcfb03ad1e10fa471b46f2b214ddbb2a",
        url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rhisat2_1.18.0.tar.gz",
    )

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-sgseq", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))

    def setup_build_environment(self, env):
        # the build does not work when conducted in parallel
        env.set("MAKEFLAGS", "-j1")
