# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySavana(PythonPackage):
    """SAVANA - somatic structural variant caller for long reads."""

    homepage = "https://github.com/cortes-ciriano-lab/savana"
    git = "https://github.com/cortes-ciriano-lab/savana.git"
    url = "https://github.com/cortes-ciriano-lab/savana/archive/refs/tags/1.3.6.tar.gz"

    license("Apache-2.0")

    version("1.3.6", sha256="8db4cb33baf3c71622c0508382e579dd9d83f1b6d9d57cbd3e1027b59b0a40a7")
    version("1.3.5", sha256="149067ec4806729e35707ed07d740aa0d2a188d2bf24be5d3a3c615112060904")

    def url_for_version(self, version):
        return (
            f"https://github.com/cortes-ciriano-lab/savana/archive/refs/tags/{version}.tar.gz"
        )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pybedtools@0.9.0:", type=("build", "run"))
    depends_on("py-pysam@0.20.0:", type=("build", "run"))
    depends_on("py-cyvcf2@0.30.16:", type=("build", "run"))
    depends_on("py-scikit-learn@1.2.2:", type=("build", "run"))
    depends_on("py-pandas@2.0.0:", type=("build", "run"))
    depends_on("py-matplotlib@3.7.1:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            savana = Executable(join_path(self.prefix.bin, "savana"))
            savana("--help")
