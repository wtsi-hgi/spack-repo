# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Plmc(MakefilePackage):
    """PLMC infers undirected graphical models to describe coevolution and
    covariation in families of biological sequences."""

    homepage = "https://github.com/debbiemarkslab/plmc"
    url = "https://github.com/debbiemarkslab/plmc/archive/refs/heads/master.tar.gz"
    git = "https://github.com/debbiemarkslab/plmc.git"

    maintainers("@johnbintz")

    version("20230121", commit="18c9e55e3bd2f14f4968be19a807b401996c929a")

    variant("openmp", default=True, description="Build with OpenMP support")
    variant(
        "precision", default="double", description="Floating point precision", values=("single", "double"), multi=False
    )

    def build(self, spec, prefix):
        if spec.platform == "darwin":
            if "+openmp" in spec:
                if spec.variants["precision"].value == "single":
                    make("all-mac-openmp32")
                else:
                    make("all-mac-openmp")
            else:
                if spec.variants["precision"].value == "single":
                    make("all-mac32")
                else:
                    make("all-mac")
        else:
            if "+openmp" in spec:
                if spec.variants["precision"].value == "single":
                    make("all-openmp32")
                else:
                    make("all-openmp")
            else:
                if spec.variants["precision"].value == "single":
                    make("all32")
                else:
                    make("all")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("bin/plmc", prefix.bin)
