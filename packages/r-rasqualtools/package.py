# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasqualtools(RPackage):
    """Prepare read counts and gene metadata for RASQUAL.

    rasqualTools exports read counts and gene metadata in RASQUAL's binary
    format and imports results from tabix-indexed tab-separated output files.
    """

    homepage = "https://github.com/kauralasoo/rasqual/tree/master/rasqualTools"
    git = "https://github.com/kauralasoo/rasqual.git"

    version("20170728", commit="05c3a1e38f75679cce5e0806640cfd250363eede")

    depends_on("r@3.2.2:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))

    def install(self, spec, prefix):
        R(
            "--vanilla",
            "CMD",
            "INSTALL",
            "--library={0}".format(self.module.r_lib_dir),
            join_path(self.stage.source_path, "rasqualTools"),
        )
