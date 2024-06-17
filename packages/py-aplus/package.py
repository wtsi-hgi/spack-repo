# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAplus(PythonPackage):
    """"""

    pypi = "aplus/aplus-0.11.0.tar.gz"

    version("0.11.0", sha256="4f57025413bd9611fb54782b8f46946ea874ae7bb6dd876c0ec45c6a8d60f6e7")

    depends_on("py-setuptools", type="build")
