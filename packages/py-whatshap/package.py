# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyWhatshap(PythonPackage):
    """WhatsHap is a software for phasing genomic variants using DNA
    sequencing reads, also called read-based phasing or haplotype
    assembly."""

    homepage = "https://whatshap.readthedocs.io/en/latest/"
    url = "https://bitbucket.org/whatshap/whatshap/get/v0.17.tar.gz"

    license("MIT")

    version("0.17", sha256="5f342cbd28f5d3e79490754f067aa67e8bb059da1c042d944b9f75663ef6b055")

    # depends_on("cxx", type="build")  # generated

    depends_on("python@3.4:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython@0.17:", type=("build", "run"))
    depends_on("py-pysam@0.14.0:", type="run")
    depends_on("py-xopen", type="run")
    depends_on("py-pyvcf", type="run")
    depends_on("py-pyfaidx", type="run")
    depends_on("py-networkx", type="run")

    def patch(self):
        # there is a stray \xe2 somewhere in setup.py,
        # explicitly using utf-8 will let the install proceed
        filter_file('^"""$', '#coding: utf-8\n"""', "setup.py")
        filter_file(
            'self.extensions = cythonize(self.extensions)',
            'self.extensions = cythonize(self.extensions, include_path=["whatshap"])',
            "setup.py",
            string=True,
        )
        filter_file(
            "cythonize(extensions)",
            'cythonize(extensions, include_path=["whatshap"])',
            "setup.py",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        whatshap = Executable(join_path(self.prefix.bin, "whatshap"))
        with working_dir("spack-test", create=True):
            whatshap("--help")
