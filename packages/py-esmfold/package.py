# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEsmfold(PythonPackage):
    """Evolutionary Scale Modeling"""

    homepage = "https://github.com/facebookresearch/esm"
    git = "https://github.com/facebookresearch/esm"

    version("2.0.1", commit="2b36991")

    # check environment.yml for dependencies
    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("openmm@7.7", type=("build", "run"))
    depends_on("py-pdbfixer", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-fairscale", type=("build", "run"))
    depends_on("py-omegaconf", type=("build", "run"))
    depends_on("py-hydra-core", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("hmmer@3.3.2", type=("build", "run"))

    depends_on("hh-suite@3.3.0", type=("build", "run"))
    depends_on("kalign", type=("build", "run"))

    depends_on("py-biopython@1.79", type=("build", "run"))

    # depends_on("py-deepspeed@0.5.9", type=("build", "run"))
    depends_on("py-deepspeed", type=("build", "run"))

    depends_on("py-dm-tree@0.1.6", type=("build", "run"))
    depends_on("py-ml-collections@0.1.0", type=("build", "run"))

    # depends_on("py-numpy@1.21.2", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    depends_on("py-pyyaml@5.4.1", type=("build", "run"))
    depends_on("py-requests@2.26.0", type=("build", "run"))
    depends_on("py-scipy@1.7.1", type=("build", "run"))
    depends_on("py-tqdm@4.62.3", type=("build", "run"))
    depends_on("py-typing-extensions@3.10.0.2", type=("build", "run"))
    depends_on("py-pytorch-lightning@1.5.3", type=("build", "run"))
    depends_on("py-wandb@0.13.9", type=("build", "run"))

    depends_on("py-dllogger", type=("build", "run"))
    depends_on("py-openfold", type=("build", "run"))
    depends_on("py-modelcif", type=("build", "run"))
