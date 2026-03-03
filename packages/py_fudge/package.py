# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFudge(PythonPackage):
    """Replace real objects with fakes (mocks, stubs, etc) while testing."""

    homepage = "https://github.com/fudge-py/fudge"
    pypi = "fudge/fudge-1.1.1.tar.gz"

    license("MIT")

    version("0.9.0", sha256="83b12d1c6da52d536167f65c95b7ecaaeebd860789f8d9e35e70a1a7e4926fba")
    version("0.9.1", sha256="4c0a0711d634a0f250c4bbe7c866de8adbaf7e944942a858c4a051ff26a19397")
    version("0.9.2", sha256="12c4b49f2cda52cf970c86f731494a7dde7a74f6c2cdf82844fca5cd3848c036")
    version("0.9.3", sha256="cf99ae86b2fb3d65184857fa0139d1c25fcbb168de34ae9a62735fad44d6bd16")
    version("0.9.4", sha256="7c8cf89e8ca1f2923ef5e139e9a37d347a135fb0161275b946a4fe5b4d17520f")
    version("0.9.5", sha256="a44e5de286c586ac9e08ca7f15e6ebe94ba2f0e55f6c2d1e24856ca53b8ef1d1")
    version("0.9.6", sha256="34690c4692e8717f4d6a2ab7d841070c93c8d0ea0d2615b47064e291f750b1a0")
    version("1.0.0", sha256="5a4ab4e1756164d3f07675d878f66a278e606eeb74757a6795ce8979fb19a68f")
    version("1.0.1", sha256="2396e62c52fb5502c3fd84e1c81cba8ed31ecc4e09063f60624f195523298531")
    version("1.0.2", sha256="817299799d1a9486316ad8b23973cd021e346578c2b446495152883f140a41a3")
    version("1.0.3", sha256="f8c8bfb3c0199dd06108c0c5a80e3645c7a071e0917b1a3bc73c761800809251")
    version("1.1.0", sha256="eba59a926fa1df1ab6dddd69a7a8af21865b16cad800cb4d1af75070b0f52afb")
    version("1.1.1", sha256="d9929d87bb38711112734d99a2c7ada5dc39ef67b758b1e55f4c779c3634efdc")

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    def patch(self):
        """Modernize the upstream sources for Python 3 without setuptools' use_2to3."""
        python = self.spec["python"].command
        with working_dir(self.stage.source_path):
            python("-m", "lib2to3", "-w", "-n", "fudge")
            python("-m", "lib2to3", "-w", "-n", "setup.py")
            filter_file(
                "    extra_setup['use_2to3'] = True",
                "    pass",
                "setup.py",
                string=True,
            )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import fudge")
