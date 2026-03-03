# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKneed(PythonPackage):
    """Knee-point detection in Python"""

    homepage = "https://github.com/arvkevi/kneed"
    pypi = "kneed/kneed-0.8.5.tar.gz"
    git = "https://github.com/arvkevi/kneed"

    version("0.8.5", sha256="a4847ac4f1d04852fea278d5de7aa8bfdc3beb7fbca4a182fec0f0efee43f4b1")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-hatchling", type=("build", "run"))
