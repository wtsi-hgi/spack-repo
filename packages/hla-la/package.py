# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class HlaLa(MakefilePackage):
    """HLA*LA carries out HLA typing based on a population reference graph and employs a new linear projection method to align reads to the graph."""

    homepage = "https://github.com/DiltheyLab/HLA-LA"
    url = "https://github.com/DiltheyLab/HLA-LA/archive/refs/tags/v1.0.3.tar.gz"

    version("1.0.3", sha256="bd2434616597aecfb38ec5b3b0e1e9812fa51c5dbf8fcdb2208d53cf694b9785")
    version("1.0.2", sha256="ddcaecb2a96f62a98b69ab725589afe722a77df927e0e9830e013cfa49548d16")
    version("1.0.1", sha256="4c615dd6be32f52a60037a76ab3cfb62f95531b754aa4c78b2377efcf6074478")
    version("1.0", sha256="8f713ee5b806e22ebeb0ae02bc19d28039d01ea7254c8c568fd3754a506f86c1")

    depends_on("gcc")
    depends_on("boost@1.59:+random+serialization+filesystem+system")
    depends_on("bamtools@2.5.1:", type=("build", "run", "link"))
    depends_on("zlib")
    depends_on("bwa@0.7.12:", type=("build", "run", "link"))
    depends_on("samtools@1.3:", type=("build", "run", "link"))
    depends_on("picard", type=("build", "run", "link"))
    depends_on("perl", type="run")

    resource(
        name="data",
        url="http://www.well.ox.ac.uk/downloads/PRG_MHC_GRCh38_withIMGT.tar.gz",
        destination="graphs",
        sha256="8e9c440fff78ac0c43172ecdb39a9b6f2e49bc0986ad5b7719435f9a533a3d38",
    )

    def patch(self):
        filter_file("../bin/HLA-LA", "/opt/view/bin/HLA-LA", "HLA-LA.pl", string=True)

    def build(self, spec, prefix):
        make("all", "BAMTOOLS_PATH=" + spec["bamtools"].prefix, "BOOSTPATH=" + spec["boost"].prefix)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.obj)
        mkdir(prefix.src)
        mkdir(prefix.graphs)

        install_tree("graphs", prefix.graphs)

        cd("..")
        install_tree("bin", prefix.bin)
        install_tree("obj", prefix.obj)
        install_tree("spack-src", prefix.src)
        install("spack-src/HLA-LA.pl", prefix.bin)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
        env.prepend_path("PATH", self.prefix.src)
