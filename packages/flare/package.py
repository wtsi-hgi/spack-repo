# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file
# for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Flare(Package):
    """Flare performs fast and memory-efficient local ancestry inference
    on phased genotype data."""

    homepage = "https://github.com/browning-lab/flare"
    git = "https://github.com/browning-lab/flare.git"

    license("Apache-2.0")
    version("20251103", commit="d6a6c8fd4479ebdb68529824acd11d2b6bbac4a1")

    depends_on("openjdk@11:", type=("build", "run"))

    def install(self, spec, prefix):
        javac = Executable(join_path(spec["openjdk"].prefix.bin, "javac"))
        jar = Executable(join_path(spec["openjdk"].prefix.bin, "jar"))
        src_dir = join_path(self.stage.source_path, "src")

        with working_dir(self.stage.source_path):
            # Compile starting from the main entry point; javac resolves deps transitively.
            javac("-cp", src_dir, join_path(src_dir, "admix", "AdmixMain.java"))
            jar("cfe", "flare.jar", "admix.AdmixMain", "-C", "src", ".")
            jar("-i", "flare.jar")

            mkdirp(prefix.libexec)
            install("flare.jar", prefix.libexec)

        mkdirp(prefix.bin)
        wrapper = join_path(prefix.bin, "flare")
        jar_path = join_path(prefix.libexec, "flare.jar")
        java_bin = join_path(spec["openjdk"].prefix.bin, "java")
        with open(wrapper, "w") as script:
            script.write("#!/bin/bash\n")
            script.write(f'exec "{java_bin}" -jar "{jar_path}" "$@"\n')
        set_executable(wrapper)

    @run_after("install")
    def install_test(self):
        java = Executable(join_path(self.spec["openjdk"].prefix.bin, "java"))
        jar_path = join_path(self.prefix.libexec, "flare.jar")
        with working_dir("spack-test", create=True):
            java("-jar", jar_path)
