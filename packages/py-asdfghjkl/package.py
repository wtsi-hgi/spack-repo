# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file
# for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyAsdfghjkl(PythonPackage):
    """ASDL provides automatic second-order differentiation utilities for
    PyTorch, covering Fisher information, Hessians, Jacobians, and related
    matrix operations."""

    homepage = "https://github.com/kazukiosawa/asdl"
    pypi = "asdfghjkl/asdfghjkl-0.1a5.tar.gz"

    maintainers("softpack-bot")
    license("MIT")
    import_modules = ["asdl"]

    version("0.1a5", sha256="02d268093bfa804132b9405266f2c3b27ffda27000b47251b31de299b13d0da8")
    version("0.1a4", sha256="a934411a0ffdee6fcdccb19672196498ea6a8e55e3e67abbe67200c84b46ddee")
    version("0.1a2", sha256="731bde1b4f19f2a370a9b284a06fd64bb897fb1beec2d8c5a8b7fa36b34e9f98")

    depends_on("python@3.7:", type=("build", "run"), when="@0.1a4:")
    depends_on("python@3.6:", type=("build", "run"), when="@:0.1a2")

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-torch@1.13:", type=("build", "run"), when="@0.1a4:")
    depends_on("py-torch@1.7:", type=("build", "run"), when="@:0.1a2")
    depends_on("py-numpy", type=("build", "run"), when="@0.1a4:")

    def patch(self):
        file = "asdl/precondition/natural_gradient.py"
        filter_file(
            "def _all_reduce_grad(self, module: nn.Module, async_op=False, op=dist.ReduceOp.SUM):",
            "def _all_reduce_grad(self, module: nn.Module, async_op=False, op=None):",
            file,
            string=True,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import asdl")
