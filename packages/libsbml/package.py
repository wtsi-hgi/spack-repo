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
#     spack install libsbml
#
# You can edit this file again by typing:
#
#     spack edit libsbml
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Libsbml(CMakePackage):
    """LibSBML is a library for reading, writing, and manipulating SBML files."""

    homepage = "https://sbml.org/Software/libSBML/"
    url = "https://github.com/sbmlteam/libsbml/archive/refs/tags/v5.18.0.tar.gz"
    git = "https://github.com/sbmlteam/libsbml.git"

    maintainers("simonqin18")

    license("LGPL-2.1-or-later")

    version("5.20.5", sha256="21c88c753a4a031f157a033de3810488b86f003e684c6ca7aa3d6e26e7e0acfc")
    version("5.20.4", sha256="02c225d3513e1f5d6e3c0168456f568e67f006eddaab82f09b4bdf0d53d2050e")
    version("5.20.2", sha256="a196cab964b0b41164d4118ef20523696510bbfd264a029df00091305a1af540")
    version("5.20.1", sha256="4463d44b55b9c05eb45248fee44b0b1391c1a563947b8d28894a426fd0df1dc9")
    version("5.20.0", sha256="400f1e1039ef0fc9addc99660a3a2559fefe9cb2c8315b1b488014b6101c438f")
    version("5.19.7", sha256="61cbdf1a86aefbc002ac5a0cf9c0f3f91eca2ae8aa5c3e7ef78be0f5a84426c5")
    version("5.19.6", sha256="77990b0f7b7419269061fbe671540c10f87f52bf8a8568953675ee615584efa6")
    version("5.19.5", sha256="6c0ec766e76bc6ad0c8626f3d208b4d9e826b36c816dff0c55e228206c82cb36")
    version("5.19.2", sha256="5b4d7a34e3d516877525041334ee9bcdd79a3dd6334d9e1a61e0687ed9751e78")
    version("5.19.0", sha256="127a44cc8352f998943bb0b91aaf4961604662541b701c993e0efd9bece5dfa8")
    # Use Git tag for 5.18.0 to avoid archive fetch issues
    version("5.18.0", tag="v5.18.0")

    # Core dependencies
    depends_on("cmake@3.16:", type="build")
    depends_on("zlib")
    depends_on("bzip2")
    depends_on("libxml2")

    # Optional but commonly needed language bindings off by default in CMake; we just build C++ core
    # Build options to disable bindings and examples/tests for lean install
    def cmake_args(self):
        args = [
            self.define("WITH_BZIP2", True),
            self.define("WITH_ZLIB", True),
            self.define("WITH_LIBXML", True),
            self.define("SWIG_EXECUTABLE", ""),
            self.define("WITH_SWIG", False),
            self.define("WITH_EXAMPLES", False),
            self.define("WITH_TESTS", False),
            self.define("WITH_CHECK", False),
            self.define("WITH_PYTHON", False),
            self.define("WITH_JAVA", False),
            self.define("WITH_CSHARP", False),
            self.define("WITH_R", False),
            self.define("WITH_PERL", False),
        ]
        return args
