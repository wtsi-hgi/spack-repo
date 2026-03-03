# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class SubsetBam(Package):
    """subset-bam is a tool to subset a 10x Genomics BAM file based on a tag, most commonly the cell barcode tag."""

    homepage = "https://github.com/10XGenomics/subset-bam"
    url = "https://github.com/10XGenomics/subset-bam/releases/download/v1.1.0/subset-bam_linux"

    version("1.1.0", sha256="05496ea56d52becdb7972528af0a486be1d52c1749e35bea9ae4c41215ed0a1b", expand=False)

    depends_on("zlib", type=("build", "link"))
    depends_on("bzip2", type=("build", "link"))
    depends_on("xz", type=("build", "link"))
    depends_on("htslib", type=("build", "link"))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        set_executable(self.stage.archive_file)
        install(self.stage.archive_file, join_path(prefix.bin, "subset_bam"))
