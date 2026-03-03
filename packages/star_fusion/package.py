# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class StarFusion(MakefilePackage):
    """STAR-Fusion is a component of the Trinity Cancer Transcriptome Analysis Toolkit (CTAT).
    STAR-Fusion uses the STAR aligner to identify candidate fusion transcripts supported by Illumina reads.
    """

    url = "https://github.com/STAR-Fusion/STAR-Fusion/releases/download/STAR-Fusion-v1.15.0/STAR-Fusion.v1.15.0.FULL.tar.gz"

    version("1.15.0", sha256="7bd1363eb8847f3fff4519a1f8bc38d2e6c11052f02736e6caf3caeced78f46e")

    depends_on("perl", type=("build", "run"))
    depends_on("r", type=("build", "run"))
    depends_on("r-ranger", type=("build", "run"))
    depends_on("r-tidyverse", type=("build", "run"))
    depends_on("star", type=("build", "run"))
    depends_on("samtools", type=("build", "run"))
    depends_on("perl-db-file", type=("build", "run"))
    depends_on("perl-uri", type=("build", "run"))
    depends_on("perl-set-intervaltree", type=("build", "run"))
    depends_on("perl-carp-assert", type=("build", "run"))
    depends_on("perl-json-xs", type=("build", "run"))
    depends_on("perl-perlio-gzip", type=("build", "run"))

    # depends_on("trinity", type=("build", "run"))

    # def edit(self, spec, prefix):
    #     # Update git submodules to use HTTPS instead of SSH
    #     gitModules = FileFilter(".gitmodules")
    #     gitModules.filter("url = git@github.com:", "url = https://github.com/")

    #     # Initialize and update submodules
    #     which("git")("submodule", "update", "--init", "--recursive")

    # def build(self, spec, prefix):
    #     make("all")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("STAR-Fusion", prefix.bin)
        install_tree("PerlLib", prefix.bin.PerlLib)
        # install_tree("")

    #     os.mkdir(prefix.bin)
    #     for exe in glob.glob("bin/*"):
    #         install(exe, prefix.bin)
