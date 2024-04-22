# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Tmscore(Package):
    """Entire source tree for the UCSC Genome Browser Group's suite of biological analysis and web display programs as well as some of Jim Kent's own tools."""

    homepage = "https://github.com/ucscGenomeBrowser/kent"
    git = "https://github.com/ucscGenomeBrowser/kent/"
    
    version("2022-02-27", sha256="0058ba45be81c56a187f72ca30c11c8127ed96dffd158a9b6caa964c680c8f86", url="https://seq2fun.dcmb.med.umich.edu//TM-score/TMscore.cpp", expand=False)

    #depends_on("libm", type=("build", "link"))

    def install(self, spec, prefix):
        bin = join_path(self.prefix, "bin")
        mkdirp(bin)

        which("g++")("-static", "-O3", "-ffast-math", "-lm", "-o", join_path(bin, "TMscore"), self.stage.archive_file)

