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
#     spack install py-dllogger
#
# You can edit this file again by typing:
#
#     spack edit py-dllogger
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyDllogger(PythonPackage):
    """This project emerged from the need for a unified logging schema for Deep Learning Example modules. It provides a simple, extensible, and intuitive logging capabilities with API trimmed to an absolute minimum."""

    homepage = "https://github.com/NVIDIA/dllogger"
    url = "https://github.com/NVIDIA/dllogger/archive/refs/tags/v1.0.0.tar.gz"

    version("1.0.0", sha256="abae2b2ac73b9e176fa87144bf6c2048ddd3dae8e7002d6d5a270bc7e4da6b4d")
    version("0.1.0", sha256="1506364a4fc0d7174db1389693600023dcfeae4b39a853758c8b690dc70738d9")

    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type=("build"))
