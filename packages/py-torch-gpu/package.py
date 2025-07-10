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
#     spack install py-torch-gpu
#
# You can edit this file again by typing:
#
#     spack edit py-torch-gpu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyTorchGpu(BundlePackage):
    """A bundle package for py-torch with cuda support."""

    version("main")
    version("2.7.1")
    version("2.7.0")
    version("2.6.0")
    version("2.5.1")
    version("2.5.0")
    version("2.4.1")
    version("2.4.0")
    version("2.3.1")
    version("2.3.0")
    version("2.2.2")
    version("2.2.1")
    version("2.2.0")
    version("2.1.2")
    version("2.1.1")
    version("2.1.0")

    depends_on("py-torch@main+cuda", type="run", when="@main")
    depends_on("py-torch@2.7.1+cuda", type="run", when="@2.7.1")
    depends_on("py-torch@2.7.0+cuda", type="run", when="@2.7.0")
    depends_on("py-torch@2.6.0+cuda", type="run", when="@2.6.0")
    depends_on("py-torch@2.5.1+cuda", type="run", when="@2.5.1")
    depends_on("py-torch@2.5.0+cuda", type="run", when="@2.5.0")
    depends_on("py-torch@2.4.1+cuda", type="run", when="@2.4.1")
    depends_on("py-torch@2.4.0+cuda", type="run", when="@2.4.0")
    depends_on("py-torch@2.3.1+cuda", type="run", when="@2.3.1")
    depends_on("py-torch@2.3.0+cuda", type="run", when="@2.3.0")
    depends_on("py-torch@2.2.2+cuda", type="run", when="@2.2.2")
    depends_on("py-torch@2.2.1+cuda", type="run", when="@2.2.1")
    depends_on("py-torch@2.2.0+cuda", type="run", when="@2.2.0")
    depends_on("py-torch@2.1.2+cuda", type="run", when="@2.1.2")
    depends_on("py-torch@2.1.1+cuda", type="run", when="@2.1.1")
    depends_on("py-torch@2.1.0+cuda", type="run", when="@2.1.0")
