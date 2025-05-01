# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpenfold(PythonPackage):
    """A faithful but trainable PyTorch reproduction of DeepMind's AlphaFold 2."""

    homepage = "https://github.com/aqlaboratory/openfold"
    git = "https://github.com/aqlaboratory/openfold"

    version("2.0.0", tag="v2.0.0")
    version("1.0.1", commit="4b41059")

    # check environment.yml for dependencies
    # depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("openmm", type=("build", "run"))
    depends_on("py-pdbfixer", type=("build", "run"))

    # cuda or cudatoolkit?
    depends_on("cuda@:11", type=("build", "run"))

    depends_on("hmmer", type=("build", "run"))
    depends_on("hh-suite", type=("build", "run"))
    depends_on("kalign", type=("build", "run"))

    # depends_on("py-torch@1.12", type=("build", "run"))
    depends_on("py-torch+cuda", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))

    # depends_on("py-deepspeed@0.5.9", type=("build", "run"))
    depends_on("py-deepspeed", type=("build", "run"))

    depends_on("py-dm-tree", type=("build", "run"))
    depends_on("py-ml-collections", type=("build", "run"))

    # depends_on("py-numpy@1.21.2", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "run", "link"))

    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-pytorch-lightning", type=("build", "run"))
    depends_on("py-wandb", type=("build", "run"))

    depends_on("awscli", type=("build", "run"))

    # depends_on("py-modelcif@0.7", type=("build", "run"))
    depends_on("py-modelcif", type=("build", "run"))

    depends_on("py-dllogger", type=("build", "run"))

    @when("@1.0.1")
    def patch(self):
        filter_file(
            "(6, 1),",
            "(6, 1), (7, 2), (8, 0), (8, 6), (8, 7), (8, 9), (9, 0)",
            "setup.py",
            string=True,
        )
        filter_file(
            "-std=c++14",
            "-std=c++17",
            "setup.py",
            string=True,
        )
