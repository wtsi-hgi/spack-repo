# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyvcf(PythonPackage):
    """A Variant Call Format reader for Python"""

    homepage = "https://pyvcf.readthedocs.org/en/latest/index.html"
    pypi = "PyVCF/PyVCF-0.6.0.tar.gz"
    license("BSD-3-Clause OR MIT")

    version("0.6.8", sha256="e9d872513d179d229ab61da47a33f42726e9613784d1cb2bac3f8e2642f6f9d9")
    version("0.6.0", sha256="d9ec3bbedb64fa35c2648a9c41fdefaedd3912ff597a436e073d27aeccf5de7c")

    depends_on("py-setuptools@62.4:", type="build", when="@0.6.8:")
    depends_on("py-setuptools@:57", type="build", when="@:0.6.0")

    def patch(self):
        filter_file("    use_2to3=True,\n", "", "setup.py", string=True)
        filter_file("from model import", "from .model import", "vcf/parser.py", string=True)
        filter_file("from parser import", "from .parser import", "vcf/sample_filter.py", string=True)
        filter_file(".iteritems()", ".items()", "vcf/parser.py", string=True)

    @run_after("install")
    def install_test(self):
        python = self.spec["python"].command
        with working_dir("spack-test", create=True):
            python("-c", "import vcf")
