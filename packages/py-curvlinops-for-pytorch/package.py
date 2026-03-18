# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file
# for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyCurvlinopsForPytorch(PythonPackage):
    """Linear operators for curvature matrices in PyTorch built on SciPy
    primitives."""

    homepage = "https://curvlinops.readthedocs.io/en/latest/"
    pypi = "curvlinops-for-pytorch/curvlinops_for_pytorch-3.0.1.tar.gz"

    maintainers("softpack-bot")
    license("MIT")
    import_modules = ["curvlinops"]

    version("3.0.1", sha256="916dd1f1a145d2fed062fcbbcc860561164bbe28b3e02174f8c7d78a006f54a7")
    version("3.0.0", sha256="52ff661821147705f66a981ea090c750ad9e4c741c06f46d8282c5e63c776066")
    version("2.0.1", sha256="2028a0542f50c40e687137930180dbb1ff87f0b798adab5d9e62b2da81b82da3")
    version("2.0.0", sha256="01f9925db9454fc9b0a31c7b83fc8ec2534c2eb12b7de7825a5298fc14e460e7")
    version(
        "1.2.0",
        sha256="d095d598397397be65e1000332854158b68fac6f992c4b396333c31924a2427d",
        url="https://files.pythonhosted.org/packages/cb/f2/dccac6ee3ca5310076c4d4a28274dad5e86254c3a99a29cec0345a12be3e/curvlinops-for-pytorch-1.2.0.tar.gz",
    )
    version(
        "1.1.0",
        sha256="b061ababf8755ff2a00a7bdb5e056433ea73b66fbf19ac84e1ed4893209542c3",
        url="https://files.pythonhosted.org/packages/8a/11/fd230ba54d84933deb9520db9681144ff252494137fe09c9c9b899b188ea/curvlinops-for-pytorch-1.1.0.tar.gz",
    )
    version(
        "1.0.0",
        sha256="def7d58fbc157f5d1a5d3375729363997d0f1d80bfd97849b4122fd61bdc76bc",
        url="https://files.pythonhosted.org/packages/f1/ab/b6493c3018a8f766b3d82edbecee8b799c983daaa1e5ba6437c46d4bb4c5/curvlinops-for-pytorch-1.0.0.tar.gz",
    )

    depends_on("python@3.10:", type=("build", "run"), when="@3:")
    depends_on("python@3.9:", type=("build", "run"), when="@2.0.1:2")
    depends_on("python@3.8:", type=("build", "run"), when="@1.2.0:2.0.0")
    depends_on("python@3.7:", type=("build", "run"), when="@:1.1.0")

    depends_on("py-setuptools@61:", type="build", when="@3:")
    depends_on("py-setuptools", type="build", when="@:2.0.1")
    depends_on("py-setuptools-scm", type="build", when="@3:")

    depends_on("py-backpack-for-pytorch@1.6:", type=("build", "run"), when="@1.2.0:")
    depends_on("py-backpack-for-pytorch@1.5:", type=("build", "run"), when="@:1.1.0")

    depends_on("py-torch@2:", type=("build", "run"), when="@1.2.0:")
    depends_on("py-torch@1.7:", type=("build", "run"), when="@:1.1.0")

    depends_on("py-scipy@1.7.1:1", type=("build", "run"), when="@1.2.0:2.0.1")
    depends_on("py-scipy@1.0:", type=("build", "run"), when="@3:")

    depends_on("py-numpy@:1", type=("build", "run"), when="@2.0.1")
    depends_on("py-numpy@1.21:", type=("build", "run"), when="@3:")

    depends_on("py-tqdm@4.61:", type=("build", "run"), when="@1.2.0:2.0.1")
    depends_on("py-tqdm@4.0:", type=("build", "run"), when="@3:")

    depends_on("py-einops", type=("build", "run"), when="@1.2.0:")
    depends_on("py-einconv", type=("build", "run"), when="@1.2.0:")
    depends_on("py-linear-operator@0.2:", type=("build", "run"), when="@3:")
    depends_on("py-opt-einsum@3.4:", type=("build", "run"), when="@3.0.1:")

    def patch(self):
        base_file = join_path("curvlinops", "_base.py")
        if not os.path.exists(base_file):
            with open(base_file, "w", encoding="utf-8") as fh:
                fh.write(
                    "from ._torch_base import *\n"
                    "from ._torch_base import PyTorchLinearOperator as _LinearOperator\n"
                )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            pyver = self.spec["python"].version.up_to(2)
            site_packages = join_path(self.prefix, f"lib/python{pyver}", "site-packages")
            env = os.environ.copy()
            pythonpaths = [site_packages]
            for dependency in self.spec.traverse(order="post", deptype=("build", "run")):
                candidate = join_path(dependency.prefix, f"lib/python{pyver}", "site-packages")
                if os.path.isdir(candidate) and candidate not in pythonpaths:
                    pythonpaths.append(candidate)
            if env.get("PYTHONPATH"):
                pythonpaths.append(env["PYTHONPATH"])
            env["PYTHONPATH"] = os.pathsep.join(pythonpaths)
            python("-c", "import curvlinops", env=env)
