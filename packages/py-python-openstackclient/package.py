# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyPythonOpenstackclient(PythonPackage):
    """OpenStack Command-line Client"""

    homepage = "https://docs.openstack.org/python-openstackclient/"
    pypi = "python-openstackclient/python_openstackclient-8.2.0.tar.gz"

    license("Apache-2.0")

    version("8.2.0", sha256="d612af18dfc66cc8f31e6ce96690b6c273ade8a240ec40b7f4835a8896fbbe01")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pbr@6.0.0:", type=("build", "run"))
    depends_on("py-cryptography@2.7:", type=("build", "run"))
    depends_on("py-cliff@4.8.0:", type=("build", "run"))
    depends_on("py-iso8601@2.0.0:", type=("build", "run"))
    depends_on("py-openstacksdk@4.6.0:", type=("build", "run"))
    depends_on("py-osc-lib@2.3.0:", type=("build", "run"))
    depends_on("py-oslo-i18n@3.15.3:", type=("build", "run"))
    depends_on("py-keystoneauth1@5.10.0:", type=("build", "run"))
    depends_on("py-python-keystoneclient@5.7.0:", type=("build", "run"))
    depends_on("py-python-cinderclient@3.3.0:", type=("build", "run"))
    depends_on("py-requests@2.27.0:", type=("build", "run"))
    depends_on("py-stevedore@5.6.0:", type=("build", "run"))

    conflicts("^py-pbr@2.1.0", msg="python-openstackclient requires pbr!=2.1.0")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            openstack_path = join_path(self.prefix.bin, "openstack")
            if not os.path.exists(openstack_path):
                raise RuntimeError(f"missing CLI at {openstack_path}")
            Executable(openstack_path)("--help")
