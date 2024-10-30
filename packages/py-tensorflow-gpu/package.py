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
#     spack install py-tensorflow-gpu
#
# You can edit this file again by typing:
#
#     spack edit py-tensorflow-gpu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyTensorflowGpu(BundlePackage):
    """A bundle package for py-tensorflow with cuda support."""

    version("2.14.0")

    depends_on("py-tensorflow@2.14.0+cuda", type="run", when="@2.14.0")
