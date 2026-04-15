# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Ibdne(Package):
    """IBDNe estimates ancestry-specific historical effective population size
    from lists of identity-by-descent segments."""

    homepage = "https://faculty.washington.edu/browning/ibdne.html"
    url = "https://faculty.washington.edu/browning/ibdne/ibdne.23Apr20.ae9.src.zip"

    license("Apache-2.0")
    version(
        "23Apr20",
        sha256="b3324ebd74ed69477067e0aec1dd22be56b1bcedbbe72d8757cda28746312665",
        url="https://faculty.washington.edu/browning/ibdne/ibdne.23Apr20.ae9.src.zip",
    )

    depends_on("openjdk@8:", type=("build", "run"))

    def install(self, spec, prefix):
        source_dir = self.stage.source_path
        src_dir = source_dir
        if os.path.isdir(join_path(source_dir, "src")):
            src_dir = join_path(source_dir, "src")
        javac = Executable(join_path(spec["openjdk"].prefix.bin, "javac"))
        jar = Executable(join_path(spec["openjdk"].prefix.bin, "jar"))

        with working_dir(self.stage.source_path):
            javac("-cp", src_dir, join_path(src_dir, "ibdne", "NeMain.java"))

            jar_name = "ibdne.jar"
            jar("cfe", jar_name, "ibdne.NeMain", "-C", src_dir, ".")
            jar("-i", jar_name)

            mkdirp(prefix.libexec)
            install(jar_name, prefix.libexec)

        mkdirp(prefix.bin)
        java_bin = join_path(spec["openjdk"].prefix.bin, "java")
        jar_path = join_path(prefix.libexec, "ibdne.jar")
        wrapper = join_path(prefix.bin, "ibdne")
        with open(wrapper, "w", encoding="utf-8") as script:
            script.write("#!/bin/bash\n")
            script.write(f'exec "{java_bin}" -jar "{jar_path}" "$@"\n')
        set_executable(wrapper)

    @run_after("install")
    def install_test(self):
        java = Executable(join_path(self.spec["openjdk"].prefix.bin, "java"))
        jar_path = join_path(self.prefix.libexec, "ibdne.jar")

        with working_dir("spack-test", create=True):
            map_path = join_path(os.getcwd(), "toy.map")
            with open(map_path, "w", encoding="utf-8") as map_file:
                map_file.write("1 marker1 0.0 1000000\n")
                map_file.write("1 marker2 5.0 5000000\n")

            ibd_path = join_path(os.getcwd(), "toy.ibd")
            with open(ibd_path, "w", encoding="utf-8") as ibd_file:
                ibd_file.write("sample1 1 sample2 1 1 1000000 5000000 1.0 5.0\n")
            java(
                "-jar",
                jar_path,
                f"map={map_path}",
                "out=toy",
                "filtersamples=false",
                "nthreads=1",
                "nboots=0",
                "gmax=10",
                "mincm=0.5",
                "minregion=0.5",
                input=ibd_path,
            )
