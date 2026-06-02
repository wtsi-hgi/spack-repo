# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEvenDist(PythonPackage):
    """Generate evenly distributed points on a sphere with Fibonacci sampling."""

    homepage = "https://github.com/tic-top/even_dist/"
    url = "https://files.pythonhosted.org/packages/47/53/aeafd99a79ac6f0aff6dde0bcac2172d4e2979711989cfef8b5d5ab80dc4/even_dist-0.3.2-py3-none-any.whl"

    license("MIT")

    version("0.3.2", sha256="1951dc9e76ab4f75a0f7767e136bd12c7e6e5fdea3791045cc3119b6f3036cb9", expand=False)

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        python = self.spec["python"].command
        with working_dir("spack-test", create=True):
            python(
                "-c",
                "import even_dist; x, y, z = even_dist.fibo_sphere(4); assert len(x) == len(y) == len(z) == 4",
            )
