# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJitOpen(PythonPackage):
    """Just in time open files"""

    homepage = "https://pypi.org/project/jit-open/"
    pypi = "jit_open/jit_open-1.0.2.tar.gz"

    version("1.0.1", sha256="069ded0d97be24641c49ba59e2c6fbe28481b1ee6c31720e64423e2f59c04dc5")
    version("1.0.2", sha256="288a220c3c7a1adaca8bb198dbb5b71e15544e792f93f0ade4df7ddda8dc69b7")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

