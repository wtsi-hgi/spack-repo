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
#     spack install py-paccmann-chemistry
#
# You can edit this file again by typing:
#
#     spack edit py-paccmann-chemistry
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPaccmannChemistry(PythonPackage):
    """Generative models of chemical data for PaccMann."""

    homepage = "https://github.com/PaccMann/paccmann_chemistry"

    url = "https://github.com/PaccMann/paccmann_chemistry/archive/refs/tags/0.0.1.tar.gz"

    license("MIT")

    version("0.0.4", sha256="3550a600770d3786ade5d64875dc63829e8e8606ee2f743e29be062f0f25d394")
    version("0.0.3", sha256="5332b5fd36fed7a1282643ff9e024a85597c0977542cb3e64fcafd45c5a6aad4")
    version("0.0.2", sha256="68efb377aa10c9a5b16b1ea9580bc2e0b8a3c7c41aa5557c301f55ef7918761e")
    version("0.0.1", sha256="9defb38ef0cee5740be9d62bcafac96c9bb37153e326d97ab24dbe2488811e16")

    depends_on("py-setuptools", type="build")
    depends_on("py-pytoda", type=("build", "run"))
    depends_on("py-absl-py", type=("build", "run"))
