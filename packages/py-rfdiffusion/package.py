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
#     spack install py-rfdiffusion
#
# You can edit this file again by typing:
#
#     spack edit py-rfdiffusion
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os

from spack.package import *


class PyRfdiffusion(PythonPackage):
    """RFdiffusion is an open source method for structure generation, with or without conditional information (a motif, target etc)."""

    homepage = "https://github.com/RosettaCommons/RFdiffusion"
    url = "https://github.com/RosettaCommons/RFdiffusion/releases/tag/v1.1.0.tar.gz"
    git = "https://github.com/RosettaCommons/RFdiffusion.git"

    license("BSD")

    version("20240826", commit="b44206a2a79f219bb1a649ea50603a284c225050")

    depends_on("py-setuptools", type="build")
    depends_on("py-se3-transformer", type=("build", "run"))
    depends_on("py-hydra-core", type=("build", "run"))
    depends_on("wget", type="build")

    @run_after("install")
    def install_config(self):
        install_tree("config", prefix.config)

    @run_after("install")
    def download_models(self):
        model_dir = os.path.join(
            self.prefix, "lib", "python{}".format(self.spec["python"].version.up_to(2)), "site-packages", "models"
        )
        mkdirp(model_dir)
        urls = [
            "http://files.ipd.uw.edu/pub/RFdiffusion/6f5902ac237024bdd0c176cb93063dc4/Base_ckpt.pt",
            "http://files.ipd.uw.edu/pub/RFdiffusion/e29311f6f1bf1af907f9ef9f44b8328b/Complex_base_ckpt.pt",
            "http://files.ipd.uw.edu/pub/RFdiffusion/60f09a193fb5e5ccdc4980417708dbab/Complex_Fold_base_ckpt.pt",
            "http://files.ipd.uw.edu/pub/RFdiffusion/74f51cfb8b440f50d70878e05361d8f0/InpaintSeq_ckpt.pt",
            "http://files.ipd.uw.edu/pub/RFdiffusion/76d00716416567174cdb7ca96e208296/InpaintSeq_Fold_ckpt.pt",
            "http://files.ipd.uw.edu/pub/RFdiffusion/5532d2e1f3a4738decd58b19d633b3c3/ActiveSite_ckpt.pt",
            "http://files.ipd.uw.edu/pub/RFdiffusion/12fc204edeae5b57713c5ad7dcb97d39/Base_epoch8_ckpt.pt",
            "http://files.ipd.uw.edu/pub/RFdiffusion/f572d396fae9206628714fb2ce00f72e/Complex_beta_ckpt.pt",
            "http://files.ipd.uw.edu/pub/RFdiffusion/1befcb9b28e2f778f53d47f18b7597fa/RF_structure_prediction_weights.pt",
        ]

        with working_dir(model_dir):
            for url in urls:
                which("wget")(url)
