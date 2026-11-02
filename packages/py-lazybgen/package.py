# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLazybgen(PythonPackage):
    """High-performance BGEN reader with cloud (GCS/S3) partial-read support"""

    homepage = "https://github.com/mkanai/lazybgen"
    pypi = "lazybgen/lazybgen-0.1.0.tar.gz"

    license("MIT")

    version("0.1.0", sha256="1ad3fc04b0fc2a6ea861bb9b2e8d3bb8194df4999d5cb5b89aa36a09aff107d1")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-cython@0.29:", type="build")
    depends_on("cmake@3.12:", type="build")
    depends_on("py-numpy@2:", type=("build", "run"))
    depends_on("py-pandas@1:", type=("build", "run"))
    depends_on("py-gcsfs@0.7:", type=("build", "run"))
    depends_on("py-fsspec@2021:", type=("build", "run"))
    depends_on("py-tqdm@4.50:", type=("build", "run"))
    depends_on("sqlite", type=("build", "link"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import lazybgen; from lazybgen import BgenReader")
