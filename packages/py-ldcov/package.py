# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLdcov(PythonPackage):
    """Efficient linkage disequilibrium calculation with covariate adjustment."""

    homepage = "https://github.com/mkanai/ldcov"
    url = "https://github.com/mkanai/ldcov/archive/refs/tags/v0.5.0.tar.gz"

    license("MIT")

    version("0.5.0", sha256="fca68e0e59b9f065aa5f9e9cead29c44d33871523b4469017b29e5461f03432a")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-setuptools-scm@6:", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-lazybgen@0.1:", type=("build", "run"))
    depends_on("py-numpy@1.19:", type=("build", "run"))
    depends_on("py-pandas@1:", type=("build", "run"))
    depends_on("py-gcsfs@0.7:", type=("build", "run"))
    depends_on("py-fsspec@2021:", type=("build", "run"))
    depends_on("py-lz4@3.1:", type=("build", "run"))
    depends_on("py-pyarrow@6:", type=("build", "run"))

    def setup_build_environment(self, env):
        env.set("SETUPTOOLS_SCM_PRETEND_VERSION", self.version)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            ldcov = Executable(self.prefix.bin.ldcov)
            ldcov("--help")

