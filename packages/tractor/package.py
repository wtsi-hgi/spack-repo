# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Tractor(Package):
    """Tractor is a local ancestry aware GWAS toolkit that provides
    utilities for extracting ancestry tracts and running ancestry-aware
    association tests."""

    homepage = "https://github.com/Atkinson-Lab/Tractor"
    url = "https://github.com/Atkinson-Lab/Tractor/archive/refs/tags/v1.4.0.tar.gz"

    license("MIT")

    version("1.4.0", sha256="7b60c5a0a893bf965761bbce5a7641f8197f81a4899725247f4d8bd6b05e60b0")

    depends_on("python@3.7:", type="run")

    depends_on("r@4.0:", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        scripts = [
            "extract_tracts.py",
            "extract_tracts_flare.py",
            "run_tractor.R",
            "unkink_2way_genofile.py",
            "unkink_2way_mspfile.py",
        ]
        for script in scripts:
            install(join_path("scripts", script), prefix.bin)
            set_executable(join_path(prefix.bin, script))

        docdir = join_path(prefix.share, "doc", "tractor")
        mkdirp(docdir)
        install("README.md", docdir)
        install("LICENSE", docdir)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "extract_tracts.py"))("--help")
            Executable(join_path(self.prefix.bin, "run_tractor.R"))("--help")
