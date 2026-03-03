# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PySouporcell(Package):
    """souporcell is a method for clustering mixed-genotype scRNAseq experiments by individual."""

    homepage = "https://github.com/wheaton5/souporcell"

    url = "https://github.com/wheaton5/souporcell/archive/refs/tags/v2.5.tar.gz"

    version("2.5", sha256="1404b87e44c4452b2f329abb81ce4a8383ed5b7e94f38ff2815c5bed62ec2c7f")
    version("1.0", sha256="40a82d1d5b2eb942c446b62e048582ff01bb7bde8e456a63fa05310106cf8202")

    depends_on("rust", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tensorflow", type=("build", "run"))
    depends_on("py-pyvcf", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-pystan", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pyfaidx", type=("build", "run"))
    depends_on("bcftools", type=("build", "run"))
    depends_on("samtools", type=("build", "run"))
    depends_on("freebayes", type=("build", "run"))
    depends_on("vartrix", type=("build", "run"))

    def install(self, spec, prefix):
        cargo = which("cargo")

        cd("troublet")
        cargo("build", "--release")
        cd("../souporcell")
        cargo("build", "--release")
        cd("..")

        installDir = prefix.opt.souporcell


        for i in ["troublet", "souporcell"]:
            dest = installDir + "/" + i + "/target/release"
            mkdirp(dest)
            install(i + "/target/release/" + i, dest)

        mkdir(prefix.bin)

        for i in ["compile_stan_model.py", "consensus.py", "reformat-smartseq.py", "renamer.py", "retag.py", "shared_samples.py", "souporcell.py", "souporcell_pipeline.py"]:
            install(i, installDir)

            installedFile = installDir + "/" + i

            os.chmod(installedFile, 0o555)

            wrapper = prefix.bin + "/" + i

            with open(wrapper, "w") as fh:
                fh.write("#!/bin/bash\npython " + installedFile)

            os.chmod(wrapper, 0o555)

        install("stan_consensus.pickle", installDir)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)

