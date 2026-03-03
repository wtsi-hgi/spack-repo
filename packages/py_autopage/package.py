# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAutopage(PythonPackage):
    """Automatic paging for command line applications."""

    homepage = "https://opendev.org/openstack/autopage"
    pypi = "autopage/autopage-0.5.2.tar.gz"

    license("Apache-2.0")

    version("0.5.2", sha256="826996d74c5aa9f4b6916195547312ac6384bac3810b8517063f293248257b72")

    depends_on("python@3.6:", type=("build", "run"))

    depends_on("py-setuptools@43:", type="build")
    depends_on("py-wheel", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import autopage")
