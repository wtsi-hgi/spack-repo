# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCliff(PythonPackage):
    """Command Line Interface Formulation Framework."""

    homepage = "https://docs.openstack.org/cliff/"
    pypi = "cliff/cliff-4.13.0.tar.gz"

    license("Apache-2.0")

    version("4.13.0", sha256="54df5434f12d3d9f0724f50feef950ee4b79ed1bd560b42fa28901a1c9656e7f")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-pbr@6.1.1:", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-autopage@0.4:", type=("build", "run"))
    depends_on("py-cmd2@3:", type=("build", "run"))
    depends_on("py-prettytable@0.7.2:", type=("build", "run"))
    depends_on("py-stevedore@5.6.0:", type=("build", "run"))
    depends_on("py-pyyaml@3.12:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import cliff.app")
