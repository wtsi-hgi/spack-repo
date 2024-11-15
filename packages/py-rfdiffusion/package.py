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

    @run_after("install")
    def install_config(self):
        install_tree("config", prefix.config)
