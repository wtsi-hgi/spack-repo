# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRmm(PythonPackage):
    """RMM: RAPIDS Memory Manager. Achieving optimal
    performance in GPU-centric workflows frequently requires
    customizing how host and device memory are allocated."""

    homepage = "https://github.com/rapidsai/rmm"
    url = "https://github.com/rapidsai/rmm/archive/v0.15.0.tar.gz"

    license("Apache-2.0")

    version("24.06.00", sha256="b7300c337b0c9a335e3386f88d6a39ed3eb8d3f66be1330ae2492c862d47aa32")
    version("24.04.00", sha256="bb20877c8d92b322dbcb348c2009040784189d3d3c48f93011e13c1b34f6a22f")
    version("24.02.00", sha256="63ddde8788727f0989f6397aed8a007ef414a577417b7d3cf39ca670c1bc4a91")
    version("23.12.00", sha256="8a274613d9d114212d7cfd74a1082d551968487208a8ad5a84de33164623359a")
    version("23.10.00", sha256="4e2408073662fdfd92ca21d87f7d2afc64d2595fd5a1e3fa321d3472cfbd7f7a")
    version("23.08.00", sha256="5bcea99a99539b9b4af0aeec7eb9f05b56ed81d439fea721f107616cc37ff640")
    version("23.06.00", sha256="3dade75a6ba21041e47493a6514513aa01d40e19bba500f5e648e399744e1a24")
    version("23.04.00", sha256="16f28d3c4ffcd6e4005bafabdd7ec3efac3aee9882f71ff758e5840294ad77ec")
    version("0.15.0", sha256="599f97b95d169a90d11296814763f7e151a8a1e060ba10bc6c8f4684a5cd7972")

    # depends_on("cxx", type="build")  # generated

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython@3:", type="build")
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-cuda-python", type=("build", "run"))
    depends_on("py-scikit-build-core@0.8:", type="build", when="@23:")
    depends_on("py-pyproject-metadata", type="build", when="@23:")
    depends_on("py-pathspec", type="build", when="@23:")

    for v in ("24.06.00", "24.04.00", "24.02.00", "23.12.00", "23.10.00", "23.08.00", "23.06.00", "23.04.00", "0.15.0"):
        depends_on("librmm@" + v, when="@"+v)

    depends_on("cuda@9:")
    depends_on("spdlog")

    conflicts("py-cython@:2", when="@23:")
    
    build_directory = "python"
    with when("@23:"):
        build_directory = "python/rmm"
