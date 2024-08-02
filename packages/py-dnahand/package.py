# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-dnahand
#
# You can edit this file again by typing:
#
#     spack edit py-dnahand
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from pathlib import Path


class PyDnahand(PythonPackage):
    """Handling DNA fingerprints validation."""

    homepage = "https://github.com/dlrice/dnahand"
    git = "https://github.com/dlrice/dnahand.git"

    version("20240801", commit="091566cf4d859671033d52f7e93d8acf886fdb19")

    # depends_on("genotyping")
    depends_on("perl-list-allutils", type=("build", "run"))
    depends_on("perl-json", type=("build", "run"))
    depends_on("perl-pod-usage", type=("build", "run"))

    depends_on("akt")
    depends_on("bcftools@1.20")
    depends_on("plink@1.9-beta6.27")

    depends_on("py-setuptools", type="build")
    depends_on("py-seaborn", type=("build", "run"))

    def patch(self):
        # fix relative paths
        for f in Path(".").glob("**/*.py"):
            for item in ["handprint", "analysis", "download", "pipeline", "utils"]:
                filter_file(f"^from {item}(?=.* import)", f"from dnahand.{item}", str(f))
                filter_file(f"^import {item}", f"import dnahand.{item}", str(f))

        with open("pyproject.toml", "w") as fh:
            fh.write(
                '[project]\nname = "DNAHAND"\nversion = "1.0"\ndependencies = []\n[project.scripts]\ndnahand = "dnahand.cli:main"'
            )

    @run_after("install")
    def install_baton(self):
        install(self.package_dir + "/baton", self.prefix.bin)
        filter_file("#!/usr/bin/env perl", f"#!{self.spec['perl'].prefix.bin.perl}", self.prefix.bin.baton, string=True)
