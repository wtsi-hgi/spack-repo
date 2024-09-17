# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCudaPython(PythonPackage):
    """Python bindings for CUDA"""
    
    homepage = "https://nvidia.github.io/cuda-python/"
    pypi = "cuda-python/" 
    url = "https://github.com/NVIDIA/cuda-python/archive/refs/tags/v11.8.0.tar.gz"

    version("12.1.0", sha256="6fdfacaabbd6bc7f5dddec3ecf6bb0968e4a6b5151896d6352703ff5e0fc4abb")
    version("12.0.0", sha256="7df0f84c4b6210112353374a7d992bfd5bba9c97358b39ea03b61bd634ce9c8a")
    version("11.8.3", sha256="f2bba3e2c7b32e2931cfcb9c85ac7fa2a051152d3b946ff4248cc7a8cb1ea553")
    version("11.8.2", sha256="8d4a4d5af7da4c99c47a1a803a3dc443e0240c867872ccb0cbb47c7013751967")
    version("11.8.0", sha256="afc4f0ac46c0e734a71f97d52390424aec1bc9fceb324e30095ca09bc678ff72")

    depends_on("py-setuptools", type="build")

    depends_on("py-cython@0.29.34:", type=("build", "run"))
    depends_on("py-pyclibrary@0.1.7:", type=("build", "run"))
    for v in ("11.8.0", "11.8.2", "11.8.3", "12.0.0", "12.1.0", "12.2.0"):
        depends_on("cuda@" + str(v), when="@" + str(v))

    def setup_build_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["cuda"].libs.directories[0])