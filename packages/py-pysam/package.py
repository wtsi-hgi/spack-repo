# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPysam(PythonPackage):
    """A python module for reading, manipulating and writing genomic data
    sets."""

    homepage = "https://github.com/pysam-developers/pysam"
    pypi = "pysam/pysam-0.14.1.tar.gz"

    version("0.22.1", sha256="18a0b97be95bd71e584de698441c46651cdff378db1c9a4fb3f541e560253b22")
    version("0.21.0", sha256="5c9645ddd87668e36ff0a1966391e26f9c403bf85b1bc06c53fe2fcd592da2ce")
    version("0.19.1", sha256="dee403cbdf232170c1e11cc24c76e7dd748fc672ad38eb0414f3b9d569b1448f")
    version("0.18.0", sha256="1d6d49a0b3c626fae410a93d4c80583a8b5ddaacc9b46a080b250dbcebd30a59")
    version("0.17.0", sha256="5d140da81ca42f474006f5cc0fd66647f1b08d559af7026bbe9f01fab029bffd")
    version("0.15.4", sha256="a535e15cbd6e27f4ab74cabca30ca1df7eea283cb91d3b536d47fe113fee066f")
    version("0.15.3", sha256="a98dd0a164aa664b1ab30a36f653752f00e93c13deeb66868597f4b2a30f7265")
    version("0.15.2", sha256="d049efd91ed5b1af515aa30280bc9cb46a92ddd15d546c9b21ee68a6ed4055d9")
    version("0.15.1", sha256="658421124c2f3de1b7445e03ca8413df0077f67ea9980abdaab0d1b5f7a8936f")
    version("0.14.1", sha256="2e86f5228429d08975c8adb9030296699012a8deba8ba26cbfc09b374f792c97")
    version("0.7.7", sha256="c9f3018482eec99ee199dda3fdef2aa7424dde6574672a4c0d209a10985755cc")

    depends_on("py-setuptools@59.0:", when="@0.21:", type="build")
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-cython@0.29.30:2", when="@0.21:", type="build")
    depends_on("py-cython@0.29.12:2", when="@0.18:", type="build")
    depends_on("py-cython@0.21:2", when="@0.14:", type="build")
    depends_on("py-cython@0.17:2", type="build")
    depends_on("curl")
    depends_on("xz")
    depends_on("htslib@1.17:", when="@0.21:")
    depends_on("htslib@1.15:1.16", when="@0.19")
    depends_on("htslib@1.14", when="@0.18")
    depends_on("htslib@1.13", when="@0.17")
    depends_on("htslib@1.9:1.12", when="@0.15")
    depends_on("htslib@1.7:1.8", when="@0.14")
    depends_on("htslib@1.6", when="@0.7")

    conflicts("py-setuptools@58.0:", when="@:0.15")

    def setup_build_environment(self, env):
        env.set("LDFLAGS", self.spec["curl"].libs.search_flags)
        # this flag is supposed to be removed by cy_build.py, but for some reason isn't
        if self.spec.platform == "darwin":
            env.remove_flags("LDSHARED", "-bundle")
        # linking htslib, see:
        # http://pysam.readthedocs.org/en/latest/installation.html#external
        # https://github.com/pysam-developers/pysam/blob/v0.9.0/setup.py#L79
        env.set("HTSLIB_MODE", "external")
        env.set("HTSLIB_LIBRARY_DIR", self.spec["htslib"].libs.directories[0])
        env.set("HTSLIB_INCLUDE_DIR", self.spec["htslib"].headers.directories[0])
