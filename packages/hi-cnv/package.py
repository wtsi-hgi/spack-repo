# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from glob import glob

class HiCnv(Package):
    """The HI-CNV software calls copy-number variants (CNVs) from SNP-array genotyping probe intensity data in large cohorts. HI-CNV uses a haplotype-informed approach that improves power to detect shorter CNVs (spanning as few as two genotyping probes) by incorporating probe data from multiple individuals who share an extended SNP haplotype—and are thus likely to also share any CNVs co-inherited within these shared genomic segments. """

    homepage = "https://data.broadinstitute.org/lohlab/HI-CNV/HI-CNV_manual.html"
    url = "https://data.broadinstitute.org/lohlab/HI-CNV/downloads/HI-CNV_v1.0.tar.gz"

    version("1.0", sha256="ed1124d63ca1b697748f17320765a589e01c006670c5cc1e68fe79c4a840ff91")

    depends_on("boost+program_options+iostreams", type=("build", "link"))
    depends_on("intel-oneapi-mkl", type=("build", "link"))
    depends_on("pkg-config", type=("build", "link"))

    patch("hash-fix.patch")

    def install(self, spec, prefix):
        mkdir(self.prefix.bin)
        mkdir(self.prefix.lib)
        mkdir(self.prefix.lib.hicnv)

        for file in glob("*.sh"):
            filter_file("./bin/", self.prefix.lib.hicnv + "/", file, string=True)
            install(file, self.prefix.bin)

        cd("src")
        filter_file("BOOST_INSTALL_DIR=/home/pl88/boost_1_58_0/install", "BOOST_INSTALL_DIR=" + spec["boost"].prefix.lib, "compile.sh", string=True)
        filter_file("MKLROOT=/n/groups/price/poru/external_software/intel_mkl_2019u4/mkl", "MKLROOT=" + spec["intel-oneapi-mkl"].prefix.lib, "compile.sh", string=True)
        which("./compile.sh")()
        cd("..")

        install_tree("bin", self.prefix.lib.hicnv)

    def setup_run_environment(self, env):
        env.append_path("PATH", self.prefix.bin)
