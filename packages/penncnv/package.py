# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from glob import glob

class Penncnv(Package):
    """PennCNV is a free software tool for Copy Number Variation (CNV) detection from SNP genotyping arrays. Currently it can handle signal intensity data from Illumina and Affymetrix arrays. With appropriate preparation of file format, it can also handle other types of SNP arrays and oligonucleotide arrays."""

    homepage = "https://penncnv.openbioinformatics.org"
    git = "https://github.com/WGLab/PennCNV"

    version("2023-12-18", commit="c86a85a6b80ce303d158773d8ec3f740e22065b3")
    
    depends_on("perl", type=("build", "link", "run"))

    def install(self, spec, prefix):
        mkdir(self.prefix.bin)
        mkdir(self.prefix.lib)
        mkdir(self.prefix.lib.penncnv)

        filter_file("use lib $_, $_.\"kext\";", "use lib \""+self.prefix.lib.penncnv+"\";", "detect_cnv.pl", string=True)

        for exe in glob("*.pl"):
            install(exe, self.prefix.bin)

        cd("kext")

        make()

        install("khmm.pm", self.prefix.lib.penncnv)

        for obj in glob("*/*/khmm.so"):
            install(obj, self.prefix.lib.penncnv)

    def setup_run_environment(self, env):
        env.append_path("PATH", self.prefix.bin)
