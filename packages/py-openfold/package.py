# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyOpenfold(PythonPackage):
    """A faithful but trainable PyTorch reproduction of DeepMind's AlphaFold 2."""

    homepage = "https://github.com/aqlaboratory/openfold"
    git = "https://github.com/aqlaboratory/openfold"

    version("2.0.0", tag="v2.0.0")
    version("1.0.1", commit="4b41059")

    # check environment.yml for dependencies
    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("openmm@7.7", type=("build", "run"))
    depends_on("py-pdbfixer", type=("build", "run"))

    # cuda or cudatoolkit?
    depends_on("cuda@11.3", type=("build", "run"))
    
    depends_on("hmmer@3.3.2", type=("build", "run"))
    depends_on("hh-suite@3.3.0", type=("build", "run"))
    depends_on("kalign", type=("build", "run"))
    
    #depends_on("py-torch@1.12", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-biopython@1.79", type=("build", "run"))
    
    #depends_on("py-deepspeed@0.5.9", type=("build", "run"))
    depends_on("py-deepspeed", type=("build", "run"))

    depends_on("py-dm-tree@0.1.6", type=("build", "run"))
    depends_on("py-ml-collections@0.1.0", type=("build", "run"))
    
    #depends_on("py-numpy@1.21.2", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    depends_on("py-pyyaml@5.4.1", type=("build", "run"))
    depends_on("py-requests@2.26.0", type=("build", "run"))
    depends_on("py-scipy@1.7.1", type=("build", "run"))
    depends_on("py-tqdm@4.62.3", type=("build", "run"))
    depends_on("py-typing-extensions@3.10.0.2", type=("build", "run"))
    depends_on("py-pytorch-lightning@1.5.3", type=("build", "run"))
    depends_on("py-wandb@0.13.9", type=("build", "run"))
   
    depends_on("awscli", type=("build", "run"))
    
    #depends_on("py-modelcif@0.7", type=("build", "run"))
    depends_on("py-modelcif", type=("build", "run"))

    depends_on("py-dllogger", type=("build", "run"))
