# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class HapIbd(Package):
    """Hap-IBD detects identity-by-descent (IBD) and homozygosity-by-descent
    (HBD) segments from phased genotype data."""

    homepage = "https://github.com/browning-lab/hap-ibd"
    url = "https://github.com/browning-lab/hap-ibd/archive/refs/tags/v1.0.0-15Jun23.92f.tar.gz"

    license("Apache-2.0")
    version(
        "1.0.0",
        sha256="9668be3580822a6da5c34fee4c04f05fa51b8471c339fc271a6404556ecc458d",
        url="https://github.com/browning-lab/hap-ibd/archive/refs/tags/v1.0.0-15Jun23.92f.tar.gz",
    )

    depends_on("openjdk@8:", type=("build", "run"))

    def install(self, spec, prefix):
        src_dir = join_path(self.stage.source_path, "src")
        javac = Executable(join_path(spec["openjdk"].prefix.bin, "javac"))
        jar = Executable(join_path(spec["openjdk"].prefix.bin, "jar"))

        with working_dir(self.stage.source_path):
            javac("-cp", src_dir, join_path(src_dir, "hapibd", "HapIbdMain.java"))
            jar("cfe", "hap-ibd.jar", "hapibd.HapIbdMain", "-C", "src", ".")
            jar("-i", "hap-ibd.jar")

            mkdirp(prefix.libexec)
            install("hap-ibd.jar", prefix.libexec)

        mkdirp(prefix.bin)
        jar_path = join_path(prefix.libexec, "hap-ibd.jar")
        java_bin = join_path(spec["openjdk"].prefix.bin, "java")
        wrapper = join_path(prefix.bin, "hap-ibd")
        with open(wrapper, "w") as script:
            script.write("#!/bin/bash\n")
            script.write(f'exec "{java_bin}" -jar "{jar_path}" "$@"\n')
        set_executable(wrapper)

    @run_after("install")
    def install_test(self):
        java = Executable(join_path(self.spec["openjdk"].prefix.bin, "java"))
        jar_path = join_path(self.prefix.libexec, "hap-ibd.jar")
        with working_dir("spack-test", create=True):
            java("-jar", jar_path)
