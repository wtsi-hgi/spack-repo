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
#     spack install py-se3-transformer
#
# You can edit this file again by typing:
#
#     spack edit py-se3-transformer
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySe3Transformer(PythonPackage):
    """This repository provides a script and recipe to train the SE(3)-Transformer model to achieve state-of-the-art accuracy. It is used as a dependency for rfdiffusion."""

    homepage = "https://github.com/RosettaCommons/RFdiffusion/tree/main/env/SE3Transformer"
    url = "https://github.com/RosettaCommons/RFdiffusion/archive/refs/tags/v1.1.0.tar.gz"

    license("BSD")

    version(
        "1.1.0",
        sha256="57d82f0d43540c2912eda3f1d34ad90b13db14966ee069c427e217fe78f0297f",
    )

    with default_args(type=("build", "run", "link")):
        depends_on("python@3.9:")
        depends_on("py-torch+cuda")
        depends_on("cuda@11:11.8")
        depends_on("py-torchaudio")
        depends_on("py-torchvision")
        depends_on("py-dgl@2+cuda backend=pytorch")
        depends_on("py-hydra-core")
        depends_on("py-pyrsistent")
        depends_on("py-decorator")
        depends_on("py-wandb")
        depends_on("py-dllogger")
        depends_on("py-e3nn")
        depends_on("py-pynvml")

    build_directory = "env/SE3Transformer"

    def setup_run_environment(self, env):
        env.append_path("LD_LIBRARY_PATH", "/opt/view/lib64")
