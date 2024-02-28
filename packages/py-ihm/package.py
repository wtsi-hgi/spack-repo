# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIhm(PythonPackage):
    """This is a Python package to assist in handling mmCIF and BinaryCIF files compliant with the integrative and hybrid modeling extension."""

    homepage = "https://github.com/ihmwg/python-ihm"
    pypi = "ihm/ihm-1.0.tar.gz"
    git = "https://github.com/ihmwg/python-ihm"

    version("1.0", sha256="d6b76b5d32c0a7034a6bb3b424df858dc5cc1e42424b57512db155ff073a89b4")
    version("0.43", sha256="bbfcbbd3f15509b5e3d3e88b49385aa00ca861259960443f41d12f39d5111af2")
    version("0.42", sha256="dc592bfef114f466b4f0ec3e3f130b2768883c5858cf28e2d0b8085b007ecc29")
    version("0.41", sha256="74b6c7ed1742571ee0241efbe56cc14fab8a84febc45a6275d55a0d258273ab0")
    version("0.40", sha256="ef33f5c089ec6bb09ace79dd395e46e90df7641f11557b05755dbac1009e0cb7")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9", type=("build", "run"))
