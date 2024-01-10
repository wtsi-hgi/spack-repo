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
#     spack install py-pyreadr
#
# You can edit this file again by typing:
#
#     spack edit py-pyreadr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyUltraplex(PythonPackage):
    """fastq demultiplexer"""

    homepage = "https://pypi.org/project/ultraplex"
    pypi = "ultraplex/ultraplex-1.2.8.tar.gz"

    version("1.2.8", sha256="2d98a070529172225be6ee1e206a2a823d59c579203029dd5438d78254a7e51e")

    depends_on("python@3.8", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("py-dnaio", type=("build", "run"))
    depends_on("py-multiprocess", type=("build", "run"))

    def patch(self):
        filter_file("get_version()", "\"1.2.8\"", "ultraplex/__main__.py", string=True)
