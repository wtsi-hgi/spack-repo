# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlashAttention(PythonPackage):
    """Fast and Memory-Efficient Exact Attention with IO-Awareness"""

    homepage = "https://github.com/Dao-AILab/flash-attention"
    git = "https://github.com/Dao-AILab/flash-attention"

    version("0.1", commit="5b838a8")
    #version("2.5.1", tag="v2.5.1")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9", type=("build", "run"))

    depends_on("py-torch@1.12", type=("build", "run"))
    depends_on("cuda@11.3", type=("build", "run"))

    #depends_on("py-packaging", type=("build", "run"))
    #depends_on("ninja", type=("build", "run"))

