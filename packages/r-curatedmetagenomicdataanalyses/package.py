# Copyright 2013-2024 Lawrence Livermore National Security, LLC and
# other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedmetagenomicdataanalyses(RPackage):
    """Analyses built on curatedMetagenomicData.

    Provides reproducible analysis workflows built on curatedMetagenomicData for
    microbiome studies, including ready-to-run scripts that combine curated
    datasets with meta-analysis utilities.
    """

    homepage = "https://github.com/waldronlab/curatedMetagenomicDataAnalyses"
    url = "https://github.com/waldronlab/curatedMetagenomicDataAnalyses/archive/refs/tags/v3.0.tar.gz"
    git = "https://github.com/waldronlab/curatedMetagenomicDataAnalyses.git"

    license("CC-BY-4.0")

    version(
        "0.4.0",
        sha256="6597cfe1d02205287522b8d27490fa9a198feddbac3277f94165a871d7641221",
        url="https://github.com/waldronlab/curatedMetagenomicDataAnalyses/archive/refs/tags/v3.0.tar.gz",
    )

    depends_on("r", type=("build", "run"))
    depends_on("r-curatedmetagenomicdata", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-meta", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        rscript = Executable(join_path(self.spec["r"].prefix.bin, "Rscript"))
        rscript("-e", 'library("curatedMetagenomicAnalyses")')
