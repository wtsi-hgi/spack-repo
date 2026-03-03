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
#     spack install py-paccmann-generator
#
# You can edit this file again by typing:
#
#     spack edit py-paccmann-generator
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPaccmannGenerator(PythonPackage):
    """Multimodal generative models for PaccMann."""

    homepage = "https://github.com/PaccMann/paccmann_generator"

    url = "https://github.com/PaccMann/paccmann_generator/archive/refs/tags/0.0.1.tar.gz"

    license("MIT")

    version("0.0.2", sha256="521421eef005e37b2e2ba0d139ee8675c0b885f78108dc25468d31c9a9c07508")
    version("0.0.1", sha256="9dce49f50db2bf8b99392ff2723db0a7a96097cd5ad1fa7acd66f5378169f919")

    depends_on("py-setuptools", type="build")
    depends_on("py-paccmann-chemistry", type=("build", "run"))
    depends_on("py-paccmann-predictor", type=("build", "run"))
    depends_on("py-paccmann-omics", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
